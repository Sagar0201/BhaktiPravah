#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Log file to store script output
LOGFILE="keep_alive.log"

# Start an infinite loop
while true; do
    echo "$(date): Sending request to BhaktiPravah" >> $LOGFILE
    curl -s https://bhaktipravah.onrender.com/ > /dev/null
    sleep 600  # Wait for 10 minutes before next request
done