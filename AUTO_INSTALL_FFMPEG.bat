@echo off
echo Running FFmpeg Auto-Installer...
echo.
echo This will install FFmpeg automatically.
echo Administrator permission required.
echo.
pause

PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& '%~dp0AUTO_INSTALL_FFMPEG.ps1'"

pause
