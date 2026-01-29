@echo off
echo Loading database content from JSON...
REM Change directory to the 'backend' folder, relative to this script
cd /d "%~dp0\.."
python manage.py migrate
python manage.py loaddata core/fixtures/core_data.json
echo Done! Your database is now in sync.
