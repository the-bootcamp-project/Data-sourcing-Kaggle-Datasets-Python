#!/bin/bash
SHELL := /bin/bash

package=sourcing_kaggle_datasets

# init-venv:
# 	python3 --version
# 	python3 -m pip install --user virtualenv
# 	python3 -m venv env
# 	(\
# 		. env/bin/activate; \
# 		which python3; \
# 		python3 -m pip install --upgrade --user -r requirements.txt; \
# 	)

init-requirements:
	python3 --version
	python3 -m pip install --upgrade --user -r requirements.txt

types:
	python3 -m mypy --version
	stubgen lib/$(package) --output lib/ --quiet
	python3 -m mypy lib/$(package)

lint:
	python3 -m pylint --version
	python3 -m pylint lib/$(package)

sast:
	python3 -m bandit --version
	python3 -m bandit -r lib/$(package) -c bandit.yml

unittests:
	python3 -m pytest --version
	python3 -m pytest

build: | types
	python3 setup.py sdist bdist_wheel

deploy:
	python3 -m twine check dist/*
	TWINE_PASSWORD=${CI_JOB_TOKEN} TWINE_USERNAME=gitlab-ci-token python3 -m twine upload --repository-url ${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/packages/pypi dist/*

release:
	python3 -m twine check dist/*
	TWINE_PASSWORD=${CI_PYPI_STABLE_TOKEN} TWINE_USERNAME=${CI_PYPI_STABLE_USER} python3 -m twine upload dist/*

version:
	python3 setup.py --version

clean:
	find . -name "__pycache__" -type d -print0 | xargs -0 /bin/rm -rf
	find . -name ".mypy_cache" -type d -print0 | xargs -0 /bin/rm -rf
	find . -name ".pytest_cache" -type d -print0 | xargs -0 /bin/rm -rf
	find . -name "*.pyi" -type f -print0 | xargs -0 /bin/rm -rf
