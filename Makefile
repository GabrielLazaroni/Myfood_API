install:
	pip install -e .['dev']

clean:
	@find ./ -name*.pyc -exec rm -f-{}^\;
	@find ./ -name'Thumbs.db'-exec rm -f{}\;
	afind ./ -name*-exec rm -f{}\;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf .egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build You,afew seconds ago
	pip install -e.[dev]--upgrade --no-cache

clean:
	pip uninstall myfood

test:
	pytest tests/ -v --cov=myfood