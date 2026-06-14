@echo off
echo ============================================================
echo   Iris Classification Project - Activating Environment
echo ============================================================
echo.

cd /d D:\DecodeLabs\Project-2-Iris-Classification

echo Activating virtual environment on D: drive...
call venv\Scripts\activate.bat

echo.
echo Running Iris Classifier...
echo.

python iris_classifier.py

echo.
echo ============================================================
echo   Project Completed!
echo ============================================================
echo.
echo Press any key to exit...
pause >nul
