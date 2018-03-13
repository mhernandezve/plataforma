PROJECT_DEFINITION := setup.py requirements.txt dev-requirements.txt

VIRTUALENV := virtualenv -p python3

PYTHON_BINS := venv/bin
PYTHON := $(PYTHON_BINS)/python
PIP := $(PYTHON_BINS)/pip
PYTEST := $(PYTHON_BINS)/pytest
TEST_FILES := scr/tests

export PATH := $(PYTHON_BINS):$(PATH)

#dependencies:
#	./bin/pip install -r requirements.txt

#test:
#	./bin/pytest -v

.PHONY: test
test:
	$(PYTEST) -v

.PHONY: install
install: | $(PYTHON) dependencies
	$(PYTHON) setup.py install

.PHONY: clean
clean:
	-rm -rf venv build dist *.egg-info .eggs
	@-rm -rf $(shell find . -name '*.pyc')

.PHONY: dependencies
dependencies: | $(PIP)
	$(PIP) install -r requirements.txt

build: dependencies test

$(PYTHON) $(PIP):
	$(VIRTUALENV) venv
