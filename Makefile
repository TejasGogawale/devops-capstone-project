.PHONY: run test lint

run:
	flask --app run:app run --host 127.0.0.1 --port 5000

test:
	nosetests

lint:
	flake8 service tests run.py
