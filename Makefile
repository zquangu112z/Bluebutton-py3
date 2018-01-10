install:
	python setup.py install

test:
	PYTHONPATH=./ python sandbox/mytest.py