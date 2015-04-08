VERSION=0.3.0

build:
	python setup.py bdist_egg

install:
	easy_install dist/bluebutton-$(VERSION)-*.egg

help:
	@echo To setup the development environment, run the following commands:
	@echo ''
	@echo 'brew list nodejs || brew install nodejs'
	@echo virtualenv venv
	@echo . venv/bin/activate
	@echo python setup.py develop
	@echo git clone https://github.com/blue-button/bluebutton.js
	@echo cd bluebutton.js
	@echo git checkout $(VERSION)
	@echo npm install
	@echo bower install
	@echo grunt test --force
	@echo 'cd ../ && make test'
	@echo ''

test:
	python setup.py nosetests

bluebutton.js:
	git clone --branch 0.3.0 https://github.com/blue-button/bluebutton.js
	sed -i'.bak' -e 's/git@github.com:chb/https:\/\/github.com\/chb/' bluebutton.js/bower.json
	cd bluebutton.js; npm install; bower install; grunt

clean:
	find bluebutton -name '*.pyc' | xargs rm
	find tests -name '*.pyc' | xargs rm
	rm -rf cover/ coverage.xml .coverage nosetests.xml
	rm -rf .eggs/ dist/ build/
