#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Start a background process to ping the website every 14 minutes
nohup bash -c 'while true; do curl -s https://bhaktipravah.onrender.com/ > /dev/null; sleep 840; done' &
