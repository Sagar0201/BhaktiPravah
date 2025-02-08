import os
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BhaktiPravah.settings")
django.setup()

def sync_databases():
    """Sync local SQLite database with the online PostgreSQL database."""
    if is_online():
        print("Syncing data with the online database...")
        call_command('dumpdata', '--database=default', output='data.json')
        call_command('loaddata', '--database=online', filename='data.json')

def is_online():
    """Check if the internet is available."""
    import socket
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False

if __name__ == "__main__":
    sync_databases()
