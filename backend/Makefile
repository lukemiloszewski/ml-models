init:
	poetry config virtualenvs.in-project true
	poetry install
	poetry run pre-commit install --hook-type pre-commit

test:
	poetry run pytest tests -v --cov

flake8:
	poetry run flake8 src tests

isort:
	poetry run isort src tests

black:
	poetry run black src tests

pre-commit:
	poetry run pre-commit run --all-files --show-diff-on-failure --color=always

requirements:
	poetry export --extras all --format requirements.txt --output requirements.txt

publish:
	poetry publish --build
