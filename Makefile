install:
	pip install -e .['dev']


test:
	pytest tests/ -v --cov=climate