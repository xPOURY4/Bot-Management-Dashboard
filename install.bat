@echo off
title Bot Manager - Installation Script
color 0B

echo ============================================================
echo   Bot Management Dashboard - Installation
echo   TheRealPourya Team
echo ============================================================
echo.
echo This script will install all required dependencies.
echo.
echo Prerequisites:
echo   - Python 3.8 or higher must be installed
echo   - Internet connection for downloading packages
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
        echo Please install Python from: https://www.python.org/
        echo Make sure to check "Add Python to PATH" during installation.
        echo.
        pause
        exit /b 1
    ) else (
        echo [OK] Python found using 'py' command
        set PYTHON_CMD=py
    )
) else (
    echo [OK] Python found using 'python' command
    set PYTHON_CMD=python
)

echo.
echo ============================================================
echo Installing Python packages...
echo ============================================================
echo.

%PYTHON_CMD% -m pip install --upgrade pip

echo.
echo Installing Flask...
%PYTHON_CMD% -m pip install Flask==3.0.0

echo.
echo Installing Flask-CORS...
%PYTHON_CMD% -m pip install Flask-CORS==4.0.0

echo.
echo Installing Werkzeug...
%PYTHON_CMD% -m pip install Werkzeug==3.0.1

echo.
echo ============================================================
echo.

REM Verify installations
echo Verifying installations...
echo.

%PYTHON_CMD% -c "import flask; print('✓ Flask:', flask.__version__)" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [!] Flask verification failed
) else (
    echo [OK] Flask installed successfully
)

%PYTHON_CMD% -c "import flask_cors; print('✓ Flask-CORS installed')" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [!] Flask-CORS verification failed
) else (
    echo [OK] Flask-CORS installed successfully
)

%PYTHON_CMD% -c "import werkzeug; print('✓ Werkzeug:', werkzeug.__version__)" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [!] Werkzeug verification failed
) else (
    echo [OK] Werkzeug installed successfully
)

echo.
echo ============================================================
echo   Installation Complete!
echo ============================================================
echo.
echo You can now run the dashboard using:
echo   - Double-click run.bat
echo   - Or run: python app.py
echo.
echo ============================================================
echo.
pause
