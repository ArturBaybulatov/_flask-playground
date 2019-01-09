@echo off

call "venv.bat"&&^
set FLASK_APP=commands.py&&^
set FLASK_DEBUG=1&&^
flask dropdb&&^
flask initdb&&^
flask generate_data

pause
