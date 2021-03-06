install:
	pipenv install --dev

run-dev:
	uvicorn main:app --reload --port 8426

test:
	TEST_ENV=True pytest tests

lint:
	flake8