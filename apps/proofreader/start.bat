@echo off
chcp 65001 > nul
cd /d "%~dp0"

echo ========================================
echo   PROOF AGENT (校正エージェント) 起動中...
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

if "%ANTHROPIC_API_KEY%"=="" (
    echo [情報] ANTHROPIC_API_KEY が未設定です。
    echo       ブラウザ画面でAPIキーを直接入力できます。
    echo.
)

echo サーバー起動中... ブラウザが自動で開きます。
echo 終了するには このウィンドウを閉じるか Ctrl+C を押してください。
echo.

:: 2秒待ってからブラウザを開く
(ping -n 3 127.0.0.1 > nul && start http://localhost:5002) &

python app.py
pause
