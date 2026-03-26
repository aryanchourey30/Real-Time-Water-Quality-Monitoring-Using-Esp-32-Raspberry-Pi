@echo off
echo Starting Water Quality Backend Server...
cd /d "%~dp0backend"
if not exist package.json (
  echo Backend folder not found.
  pause
  exit /b 1
)
npm run dev
pause
