PYTHON_VERSION := python3.11
PYTHON_BIN := $(shell which $(PYTHON_VERSION))

venv:
	$(PYTHON_BIN) -m venv venv
	venv//bin/pip install --upgrade pip
	venv/bin/pip install --editable .

lint:
	venv/bin/pip install ruff
	venv/bin/ruff --fix .

pgadmin:
	venv/bin/pip install pgadmin4
	xdg-open http://127.0.0.1:5050
	pgadmin4
