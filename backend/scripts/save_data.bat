@echo off
echo Saving database content to JSON...
cd ..
python manage.py dumpdata core --natural-foreign --natural-primary --indent 2 --output core/fixtures/core_data.json
echo Done! You can now commit the changes.
