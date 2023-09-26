# Human Centric AI-design
Run all commands from hcai/src (cd src)

## Setup

1. Install [Poetry](https://python-poetry.org/docs/).
2. Run the following command:
```
poetry install
```

## Running dev server:
```
poetry run python manage.py runserver
```

## Tailwind
https://django-tailwind.readthedocs.io/en/latest/

When running the dev server, run the following command to compile Tailwind:
```
poetry run python manage.py tailwind build
```