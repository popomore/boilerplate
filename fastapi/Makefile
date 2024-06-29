install:
	pip install -r requirements-dev.txt

dev:
	uvicorn app.main:app --reload --port=8000

test:
	pytest tests/

lint:
	ruff check --fix

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

.PHONY: install dev test lint clean
