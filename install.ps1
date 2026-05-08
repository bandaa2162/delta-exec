Write-Host "Initializing Delta Executor Setup..." -ForegroundColor Cyan

# Check if Python is installed
if (-Not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Python is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/ and try again." -ForegroundColor Yellow
    exit
}

# Create directory
$InstallDir = "$env:LOCALAPPDATA\DeltaExecutor"
if (-Not (Test-Path $InstallDir)) {
    New-Item -ItemType Directory -Path $InstallDir | Out-Null
}

Write-Host "Downloading Core Engine..." -ForegroundColor Green
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/AvenueSleuth/delta-exec/main/delta_engine.py" -OutFile "$InstallDir\delta_engine.py"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/AvenueSleuth/delta-exec/main/requirements.txt" -OutFile "$InstallDir\requirements.txt"

Write-Host "Installing dependencies..." -ForegroundColor Green
python -m pip install -r "$InstallDir\requirements.txt" -q

Write-Host "Installation Complete! Launching Delta Executor..." -ForegroundColor Magenta
Start-Sleep -Seconds 2

Set-Location -Path $InstallDir
python delta_engine.py
