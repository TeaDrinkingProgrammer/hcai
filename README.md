# Human Centric AI-design
**All the commands with manage.py need to be excecuted from the src folder (cd src)**

## Devcontainer set-up
1. Open folder in VS-code
2. When a pop up comes up asking you to open the devcontainer, select yes
3. Wait for the devcontainer start working (this may take a few minutes). Click "Open log" to see the progress
4. Start using the container.

## Non-devcontainer set-up (not reccomended)
### Setup
1. Install [Poetry](https://python-poetry.org/docs/).
2. Run the following command:
```
poetry install
```
From the src folder:
```
poetry shell
python manage.py tailwind install
python manage.py tailwind build
```

### LLVM
If you get the following error:
RuntimeError: llvm-config failed executing, please point LLVM_CONFIG to the path for llvm-config
https://stackoverflow.com/questions/61475274/runtimeerror-path-failed-executing-please-point-llvm-config-to-the-path-for
Install llvm:
```
sudo dnf install llvm
```

## Running dev server:
```
poetry shell
python manage.py runserver
```

## Tailwind
https://django-tailwind.readthedocs.io/en/latest/

When running the dev server, run the following command to compile Tailwind:
```
poetry run python manage.py tailwind build
```