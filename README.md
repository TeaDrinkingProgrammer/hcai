# Human Centric AI-design
**All the commands with manage.py need to be excecuted from the src folder (cd src)**

## Devcontainer set-up
1. Open folder in VS-code
2. When a pop up comes up asking you to open the devcontainer, select yes
3. Wait for the devcontainer start working (this may take a few minutes). Click "Open log" to see the progress
4. (Optional) Run git lfs pull if you have not done so yet
4. Start using the container.

Note: the default set-up is for docker. To use Podman, uncomment the commented out code in the devcontainer.json file. DO NOT push these changes since they will break the set-up for Docker users. TODO: more elegant solution.

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
poetry shell
python manage.py tailwind build
```

## Changes to static files
Run the following command when the static files have changed:
```
poetry shell
python manage.py collectstatic
```
If you get permission errors, you might have to rebuild the devcontainer