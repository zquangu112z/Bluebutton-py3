TEST_RUNNER:=PYTHONPATH=./ pytest --self-contained-html

install:
	python setup.py install

test:
	PYTHONPATH=./ pytest sandbox/*.py