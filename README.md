# Human Centric AI-design
**All the commands with manage.py need to be excecuted from the src folder (cd src)**

## Setup
1. Install [Poetry](https://python-poetry.org/docs/).
2. Run the following command:
```
poetry install
```
From the src folder:
```
poetry run python manage.py tailwind install
poetry run python manage.py tailwind build
```

## LLVM
If you get the following error:
RuntimeError: llvm-config failed executing, please point LLVM_CONFIG to the path for llvm-config
https://stackoverflow.com/questions/61475274/runtimeerror-path-failed-executing-please-point-llvm-config-to-the-path-for
Install llvm:
```
sudo dnf install llvm
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