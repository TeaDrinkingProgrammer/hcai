#! /bin/bash
poetry install
cd src && poetry run python manage.py tailwind install
