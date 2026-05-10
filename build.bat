@echo off
setlocal

set "APP_NAME=KeyBloom"
set "ENTRY_FILE=main.py"
set "DIST_DIR=dist"
set "BUILD_DIR=build"
set "TARGET_EXE=%DIST_DIR%\%APP_NAME%.exe"
set "VENV_PYTHON=.venv\Scripts\python.exe"
set "ICON_FILE=icon.ico"
set "ICON_ARG="
set "ADD_ICON_ARG="
set "PAUSE_ON_EXIT=1"

if /i "%~1"=="--no-pause" set "PAUSE_ON_EXIT="

echo ========================================
echo Building %APP_NAME%...
echo ========================================
echo.

if not exist "%ENTRY_FILE%" (
    echo ERROR: Entry file "%ENTRY_FILE%" not found.
    set "EXIT_CODE=1"
    goto :finish
)

if not exist "%VENV_PYTHON%" (
    echo ERROR: Python not found at "%VENV_PYTHON%".
    set "EXIT_CODE=1"
    goto :finish
)

"%VENV_PYTHON%" -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: PyInstaller is not installed in this virtual environment.
    echo Install it first with:
    echo   .venv\Scripts\python.exe -m pip install pyinstaller
    set "EXIT_CODE=1"
    goto :finish
)

if exist "%ICON_FILE%" (
    set "ICON_ARG=--icon=%ICON_FILE%"
    set "ADD_ICON_ARG=--add-data=%ICON_FILE%;."
    echo Using icon: %ICON_FILE%
)

if exist "%BUILD_DIR%" (
    echo Cleaning "%BUILD_DIR%"...
    rmdir /s /q "%BUILD_DIR%"
)

if exist "%DIST_DIR%" (
    echo Cleaning "%DIST_DIR%"...
    rmdir /s /q "%DIST_DIR%"
)

if exist "%TARGET_EXE%" (
    echo ERROR: "%TARGET_EXE%" is still locked by another process.
    echo Close KeyBloom.exe or stop the running process, then try again.
    set "EXIT_CODE=1"
    goto :finish
)

echo Running PyInstaller...
echo.

"%VENV_PYTHON%" -m PyInstaller ^
  --noconfirm ^
  --clean ^
  --onefile ^
  --windowed ^
  --name "%APP_NAME%" ^
  %ICON_ARG% ^
  %ADD_ICON_ARG% ^
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
    set "EXIT_CODE=1"
    goto :finish
)

if exist "%ICON_FILE%" (
    echo Copying %ICON_FILE% to "%DIST_DIR%"...
    copy /y "%ICON_FILE%" "%DIST_DIR%\%ICON_FILE%" >nul
    if errorlevel 1 (
        echo ERROR: Failed to copy %ICON_FILE% to "%DIST_DIR%".
        set "EXIT_CODE=1"
        goto :finish
    )
)

echo.
echo ========================================
echo Build complete.
echo Output: %DIST_DIR%\%APP_NAME%.exe
if exist "%DIST_DIR%\%ICON_FILE%" echo Icon: %DIST_DIR%\%ICON_FILE%
echo Settings path at runtime: %%APPDATA%%\%APP_NAME%\settings.json
echo ========================================
set "EXIT_CODE=0"
goto :finish

:finish
if defined PAUSE_ON_EXIT pause
endlocal
exit /b %EXIT_CODE%
