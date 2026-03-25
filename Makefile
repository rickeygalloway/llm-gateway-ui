.PHONY: install run lint format

install:
	pip install -r requirements.txt

run:
	uvicorn main:app --reload --port 3000

lint:
	ruff check .

format:
	ruff format .
