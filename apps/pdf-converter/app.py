import io
import os
import shutil
import tempfile
import threading
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_file
import pythoncom
import win32com.client

app = Flask(__name__)

ALLOWED = {'.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'}
_lock = threading.Lock()  # COM はスレッドセーフでないのでロックを使用


def _word_to_pdf(src: Path, dst: Path):
    pythoncom.CoInitialize()
    try:
        word = win32com.client.DispatchEx('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(str(src))
        doc.SaveAs(str(dst), FileFormat=17)  # 17 = wdFormatPDF
        doc.Close(False)
        word.Quit()
    finally:
        pythoncom.CoUninitialize()


def _excel_to_pdf(src: Path, dst: Path):
    pythoncom.CoInitialize()
    try:
        excel = win32com.client.DispatchEx('Excel.Application')
        excel.Visible = False
        excel.DisplayAlerts = False
        wb = excel.Workbooks.Open(str(src))
        wb.ExportAsFixedFormat(0, str(dst))  # 0 = xlTypePDF
        wb.Close(False)
        excel.Quit()
    finally:
        pythoncom.CoUninitialize()


def _ppt_to_pdf(src: Path, dst: Path):
    pythoncom.CoInitialize()
    try:
        ppt = win32com.client.DispatchEx('PowerPoint.Application')
        presentation = ppt.Presentations.Open(str(src), WithWindow=False)
        presentation.SaveAs(str(dst), 32)  # 32 = ppSaveAsPDF
        presentation.Close()
        ppt.Quit()
    finally:
        pythoncom.CoUninitialize()


def convert_to_pdf(src: Path, dst: Path):
    ext = src.suffix.lower()
    if ext in ('.doc', '.docx'):
        _word_to_pdf(src, dst)
    elif ext in ('.xls', '.xlsx'):
        _excel_to_pdf(src, dst)
    elif ext in ('.ppt', '.pptx'):
        _ppt_to_pdf(src, dst)
    else:
        raise ValueError(f'非対応の形式: {ext}')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({'error': 'ファイルがありません'}), 400

    file = request.files['file']
    if not file.filename:
        return jsonify({'error': 'ファイル名が空です'}), 400

    suffix = Path(file.filename).suffix.lower()
    if suffix not in ALLOWED:
        return jsonify({'error': f'非対応の形式です: {suffix}'}), 400

    pdf_name = Path(file.filename).stem + '.pdf'

    tmpdir = Path(tempfile.mkdtemp())
    try:
        src = tmpdir / file.filename
        dst = tmpdir / pdf_name
        file.save(str(src))

        with _lock:
            convert_to_pdf(src, dst)

        pdf_bytes = io.BytesIO(dst.read_bytes())
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    pdf_bytes.seek(0)
    return send_file(
        pdf_bytes,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=pdf_name,
    )


if __name__ == '__main__':
    app.run(port=5001, debug=False)
