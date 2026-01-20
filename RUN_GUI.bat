@echo off
echo ========================================
echo  VIDEO DOWNLOADER - GUI VERSION
echo ========================================
echo.
echo Starting GUI application...
echo.
py video_downloader_gui.py
if errorlevel 1 (
    echo.
    echo ERROR: Python not found!
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
)
pause
