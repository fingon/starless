all: test

test: .done.test

.done.test: $(wildcard *.py */*.py)
	py.test
	touch $@

.done.dist: .done.test
	rm -rf dist
	python3 setup.py sdist bdist_wheel
	touch $@

u-test-pypi: .done.dist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

u-pypi: .done.dist
	twine upload dist/*
