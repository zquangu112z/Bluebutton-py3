install:
	python setup.py install

test:
	PYTHONPATH=./ pytest ./sandbox/*.py