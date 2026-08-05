@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
  py -3 apply_patch.py
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    python apply_patch.py
  ) else (
    echo Python 3 was not found.
    echo Install Python 3 and run this file again.
  )
)

echo.
pause
