@echo off
chcp 65001 > nul
cd /d "%~dp0"

echo ========================================
echo   PDF Converter を起動しています...
echo ========================================
echo.

python --version > nul 2>&1
if errorlevel 1 (
    echo [エラー] Python が見つかりません。
    echo https://www.python.org からインストールしてください。
    pause
    exit /b 1
)

echo 依存パッケージを確認中...
pip install -r requirements.txt -q
echo.
echo サーバー起動中... ブラウザが自動で開きます。
echo 終了するには このウィンドウを閉じるか Ctrl+C を押してください。
echo.

:: 2秒待ってからブラウザを開く
(ping -n 3 127.0.0.1 > nul && start http://localhost:5001) &

python app.py
pause
