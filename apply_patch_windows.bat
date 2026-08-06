@echo off
setlocal
cd /d "%~dp0"
chcp 65001 >nul

where powershell.exe >nul 2>nul
if errorlevel 1 (
  echo Windows PowerShell was not found.
  echo This portable installer supports Windows 10 and Windows 11 x86-64.
  echo See README_FIRST_KO.txt for manual installation instructions.
  echo.
  pause
  exit /b 2
)

powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0apply_patch_windows.ps1" %*
set "PATCH_EXIT=%ERRORLEVEL%"
echo.
pause
exit /b %PATCH_EXIT%
