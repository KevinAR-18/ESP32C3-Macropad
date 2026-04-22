@echo off
setlocal

set "APP_NAME=KeyBloom"
set "ENTRY_FILE=main.py"
set "DIST_DIR=dist"
set "BUILD_DIR=build"
set "VENV_PYINSTALLER=.venv\Scripts\pyinstaller.exe"

echo ========================================
echo Building %APP_NAME%...
echo ========================================
echo.

if not exist "%ENTRY_FILE%" (
    echo ERROR: Entry file "%ENTRY_FILE%" not found.
    exit /b 1
)

if not exist "%VENV_PYINSTALLER%" (
    echo ERROR: PyInstaller not found at "%VENV_PYINSTALLER%".
    echo Install it first with:
    echo   .venv\Scripts\python.exe -m pip install pyinstaller
    exit /b 1
)

if exist "%BUILD_DIR%" (
    echo Cleaning "%BUILD_DIR%"...
    rmdir /s /q "%BUILD_DIR%"
)

if exist "%DIST_DIR%" (
    echo Cleaning "%DIST_DIR%"...
    rmdir /s /q "%DIST_DIR%"
)

echo Running PyInstaller...
echo.

"%VENV_PYINSTALLER%" ^
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
    echo.
    echo ========================================
    echo ERROR: Build failed.
    echo ========================================
    exit /b 1
)

echo.
echo ========================================
echo Build complete.
echo Output: %DIST_DIR%\%APP_NAME%.exe
echo Settings path at runtime: %%APPDATA%%\%APP_NAME%\settings.json
echo ========================================
endlocal
exit /b 0
