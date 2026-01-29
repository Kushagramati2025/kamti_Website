@echo off
echo Saving database content to JSON...
REM Change directory to the 'backend' folder, relative to this script
cd /d "%~dp0\.."
python manage.py dumpdata core --natural-foreign --natural-primary --indent 2 --output core/fixtures/core_data.json
echo Done! You can now commit the changes.
