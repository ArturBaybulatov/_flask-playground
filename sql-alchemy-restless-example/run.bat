@echo off

call "venv.bat"&&^
set FLASK_APP=main.py&&^
set FLASK_DEBUG=1&&^
flask run --port 8666

pause
