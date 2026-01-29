@echo off
echo Loading database content from JSON...
cd ..
python manage.py migrate
python manage.py loaddata core/fixtures/core_data.json
echo Done! Your database is now in sync.
