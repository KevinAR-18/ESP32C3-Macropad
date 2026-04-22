@echo off
setlocal

rem Example build script for KeyBloom.
rem Copy this pattern if later you want a debug/release variant.

set "APP_NAME=KeyBloom"
set "ENTRY_FILE=main.py"
set "PYINSTALLER=.venv\Scripts\pyinstaller.exe"

echo ========================================
echo Example build for %APP_NAME%
echo ========================================
echo.

if not exist "%PYINSTALLER%" (
    echo PyInstaller not found.
    echo Install with:
    echo   .venv\Scripts\python.exe -m pip install pyinstaller
    exit /b 1
)

"%PYINSTALLER%" ^
  --noconfirm ^
  --clean ^
  --onefile ^
  --windowed ^
  --name "%APP_NAME%" ^
  --hidden-import=keyboard ^
  --hidden-import=psutil ^
  --hidden-import=pycaw.pycaw ^
  --hidden-import=serial.tools.list_ports ^
  --hidden-import=comtypes ^
  "%ENTRY_FILE%"

if errorlevel 1 (
    echo Build failed.
    exit /b 1
)

echo Build finished: dist\%APP_NAME%.exe
echo Settings will be saved to: %%APPDATA%%\%APP_NAME%\settings.json
endlocal
exit /b 0
