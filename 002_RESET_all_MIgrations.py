import os
import django
import shutil
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fantasyfootball.settings')
django.setup()

from django.apps import apps

for app in apps.get_app_configs():
    app_path = app.module.__file__
    app_dir = os.path.dirname(app_path)

    # skip Django apps
    if "django" in app_path:
        continue

    print(app.label)

    APP_NAME = app.label

    # get path to app/migrations directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    migrations_path = os.path.join(app_dir, APP_NAME, 'migrations')

    # loop through files in migrations directory and delete all except __init__.py
    for filename in os.listdir(migrations_path):
        if filename != '__init__.py':
            file_path = os.path.join(migrations_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
