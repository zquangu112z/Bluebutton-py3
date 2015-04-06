help: develop

develop:
	@echo To setup the development environment, run the following commands:
	@echo ''
	@echo 'brew list nodejs || brew install nodejs'
	@echo virtualenv venv
	@echo . venv/bin/activate
	@echo python setup.py develop
	@echo git clone https://github.com/blue-button/bluebutton.js
	@echo cd bluebutton.js
	@echo git checkout 0.3.0
	@echo npm install
	@echo bower install
	@echo grunt test --force
	@echo 'cd ../ && make test'
	@echo ''

test:
	python setup.py nosetests

clean:
	find bluebutton -name '*.pyc' | xargs rm
	find tests -name '*.pyc' | xargs rm
	rm -rf cover/ coverage.xml .coverage nosetests.xml
	rm -rf .eggs/