@echo off
title Bot Manager - Build Executable
color 0E

echo ============================================================
echo   Bot Management Dashboard - Build Script
echo   TheRealPourya Team
echo ============================================================
echo.
echo This script will build a standalone .exe file using PyInstaller
echo.
echo ============================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    py --version >nul 2>&1
    if %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Python is not installed or not in PATH!
        echo.
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=py
    )
) else (
    set PYTHON_CMD=python
)

echo [OK] Python detected
echo.

REM Check if PyInstaller is installed
%PYTHON_CMD% -m pip show pyinstaller >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] PyInstaller not found. Installing...
    echo.
    %PYTHON_CMD% -m pip install pyinstaller
    echo.
) else (
    echo [OK] PyInstaller is installed
    echo.
)

REM Clean previous builds
echo ============================================================
echo Cleaning previous builds...
echo ============================================================
echo.

if exist "build" (
    echo Removing build folder...
    rmdir /s /q build
)

if exist "dist" (
    echo Removing dist folder...
    rmdir /s /q dist
)

if exist "BotManager.exe" (
    echo Removing old executable...
    del /f /q BotManager.exe
)

echo.
echo ============================================================
echo Building executable...
echo ============================================================
echo.
echo This may take a few minutes. Please wait...
echo.

REM Build using the spec file
%PYTHON_CMD% -m PyInstaller --clean BotManager.spec

echo.
echo ============================================================

REM Check if build was successful
if exist "dist\BotManager.exe" (
    echo.
    echo [SUCCESS] Build completed successfully!
    echo.
    echo Executable location: dist\BotManager.exe
    echo.
    echo You can now:
    echo   1. Run dist\BotManager.exe to test
    echo   2. Distribute dist\BotManager.exe to users
    echo.
    echo Note: Users do NOT need Python installed to run the .exe
    echo.

    REM Optional: Move exe to root folder
    echo ============================================================
    echo.
    choice /C YN /M "Do you want to copy BotManager.exe to the current folder"
    if errorlevel 2 goto end
    if errorlevel 1 (
        copy "dist\BotManager.exe" "BotManager.exe"
        echo.
        echo [OK] BotManager.exe copied to current folder
    )
) else (
    echo.
    echo [ERROR] Build failed! Please check the errors above.
    echo.
    echo Common issues:
    echo   - Missing dependencies: Run install.bat first
    echo   - Missing templates or static folders
    echo   - Incorrect PyInstaller configuration
    echo.
)

:end
echo.
echo ============================================================
echo.
pause
