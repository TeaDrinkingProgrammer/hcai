#! /bin/bash
poetry install
cd src && poetry run python manage.py tailwind install
poetry run python manage.py collectstatic --no-input