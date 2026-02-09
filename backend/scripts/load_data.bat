@echo off
echo Loading database content from JSON...
cd /d "%~dp0.."
python manage.py migrate
python scripts/fix_encoding.py
python manage.py loaddata core/fixtures/core_data.json
echo Done! Your database is now in sync.
