install:
	python setup.py install

test:
	PYTHONPATH=./ pytest ./tests/*.py