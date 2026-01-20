@echo off
echo ========================================
echo  CREATE EXE FILE
echo  Video Downloader GUI
echo ========================================
echo.

echo [1/2] Installing PyInstaller...
py -m pip install pyinstaller
if errorlevel 1 (
    echo ERROR: Failed to install PyInstaller
    pause
    exit /b 1
)
echo.

echo [2/2] Creating EXE file...
echo This may take a few minutes...
echo.

py -m PyInstaller --onefile --windowed --name "VideoDownloader" --icon=NONE video_downloader_gui.py

echo.
echo ========================================
echo EXE Creation Complete!
echo ========================================
echo.
echo Your EXE file is located in the "dist" folder:
echo dist\VideoDownloader.exe
echo.
echo You can now:
echo 1. Copy VideoDownloader.exe to any location
echo 2. Double-click it to run (no Python needed!)
echo 3. Share it with others
echo.
pause
