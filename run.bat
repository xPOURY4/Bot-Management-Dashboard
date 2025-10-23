@echo off
title Bot Management Dashboard - TheRealPourya Team
color 0A

echo ============================================================
echo   Bot Management Dashboard - TheRealPourya Team
echo ============================================================
echo.
echo Starting Flask server...
echo.

REM Start the Python Flask application
python app.py

REM If Python command fails, try py command
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Python not found with 'python' command, trying 'py'...
    py app.py
)

REM Keep window open if there's an error
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ============================================================
    echo ERROR: Failed to start the dashboard!
    echo.
    echo Please make sure Python is installed and requirements are met.
    echo Run: pip install -r requirements.txt
    echo ============================================================
    echo.
    pause
)
