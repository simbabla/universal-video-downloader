Write-Host "========================================" -ForegroundColor Cyan
Write-Host " FFMPEG AUTO-INSTALLER" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERROR: This script must be run as Administrator!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Right-click on PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit
}

# Define paths
$downloadUrl = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
$zipFile = "$env:TEMP\ffmpeg.zip"
$extractPath = "$env:TEMP\ffmpeg-extract"
$installPath = "C:\ffmpeg"

Write-Host "[1/5] Downloading FFmpeg..." -ForegroundColor Yellow
try {
    Invoke-WebRequest -Uri $downloadUrl -OutFile $zipFile -UseBasicParsing
    Write-Host "Download complete!" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to download FFmpeg: $_" -ForegroundColor Red
    pause
    exit
}

Write-Host ""
Write-Host "[2/5] Extracting files..." -ForegroundColor Yellow
try {
    if (Test-Path $extractPath) { Remove-Item $extractPath -Recurse -Force }
    Expand-Archive -Path $zipFile -DestinationPath $extractPath -Force
    Write-Host "Extraction complete!" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to extract: $_" -ForegroundColor Red
    pause
    exit
}

Write-Host ""
Write-Host "[3/5] Installing to C:\ffmpeg..." -ForegroundColor Yellow
try {
    # Find the extracted folder (it has a version number in the name)
    $ffmpegFolder = Get-ChildItem -Path $extractPath -Directory | Select-Object -First 1
    
    # Create install directory if it doesn't exist
    if (-not (Test-Path $installPath)) {
        New-Item -ItemType Directory -Path $installPath -Force | Out-Null
    }
    
    # Copy files
    Copy-Item -Path "$($ffmpegFolder.FullName)\*" -Destination $installPath -Recurse -Force
    Write-Host "Installation complete!" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to install: $_" -ForegroundColor Red
    pause
    exit
}

Write-Host ""
Write-Host "[4/5] Adding to system PATH..." -ForegroundColor Yellow
try {
    $binPath = "$installPath\bin"
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    
    if ($currentPath -notlike "*$binPath*") {
        $newPath = "$currentPath;$binPath"
        [Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")
        Write-Host "Added to PATH!" -ForegroundColor Green
    } else {
        Write-Host "Already in PATH!" -ForegroundColor Green
    }
} catch {
    Write-Host "ERROR: Failed to update PATH: $_" -ForegroundColor Red
    Write-Host "You may need to add C:\ffmpeg\bin to PATH manually" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "[5/5] Cleaning up..." -ForegroundColor Yellow
Remove-Item $zipFile -Force -ErrorAction SilentlyContinue
Remove-Item $extractPath -Recurse -Force -ErrorAction SilentlyContinue
Write-Host "Cleanup complete!" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " INSTALLATION COMPLETE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Close ALL PowerShell/Terminal windows" -ForegroundColor White
Write-Host "2. Restart your Video Downloader GUI" -ForegroundColor White
Write-Host "3. Try downloading a video again!" -ForegroundColor White
Write-Host ""
Write-Host "To verify installation (in a NEW terminal):" -ForegroundColor Yellow
Write-Host "  ffmpeg -version" -ForegroundColor White
Write-Host ""
pause
