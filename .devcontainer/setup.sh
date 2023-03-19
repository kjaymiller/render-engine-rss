python -m pip install --user --upgrade pip
python -m pip install --user -r .devcontainer/requirements.txt pip-tools
python -m piptools compile --upgrade --extra=dev pyproject.toml 
python -m pip install --user -r requirements.txt
