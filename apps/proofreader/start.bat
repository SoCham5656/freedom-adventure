@echo off
cd /d "%~dp0"

echo ========================================
echo   PROOF AGENT - Starting...
echo ========================================
echo.

python --version
if errorlevel 1 (
    echo [ERROR] Python not found.
    pause
    exit /b 1
)

echo Installing packages...
python -m pip install flask anthropic pdfplumber python-pptx python-docx
if errorlevel 1 (
    echo [ERROR] pip install failed.
    pause
    exit /b 1
)

echo.
echo Starting server at http://localhost:5002
echo Press Ctrl+C to stop.
echo.

(ping -n 3 127.0.0.1 > nul && start http://localhost:5002) &

python app.py
pause
