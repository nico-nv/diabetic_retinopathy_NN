# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* diabetic_retinopathy_NN/*.py

black:
	@black scripts/* diabetic_retinopathy_NN/*.py

#NN: + "test_"
test:
	@coverage run -m pytest tests/test_*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr diabetic_retinopathy_NN-*.dist-info
	@rm -fr diabetic_retinopathy_NN.egg-info

install:
	@pip install . -U

all: clean install test black check_code

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
PYPI_USERNAME=<AUTHOR>
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

pypi:
	@twine upload dist/* -u $(PYPI_USERNAME)

# ----------------------------------
#      Prediction API
# ----------------------------------
#NN: + run_api
run_api:
	uvicorn api.fast:app --reload  # load web server with code autoreload

#NN: + Heroku Commands
# ----------------------------------
#         HEROKU COMMANDS
# ----------------------------------

streamlit:
	-@streamlit run app.py

heroku_login:
	-@heroku login

heroku_upload_public_key:
	-@heroku keys:add ~/.ssh/id_ed25519.pub

#NN: APP_NAME = diabetic-retinopathy-nn
heroku_create_app:
	-@heroku create --ssh-git ${diabetic-retinopathy-nn}

deploy_heroku:
	-@git push heroku master
	-@heroku ps:scale web=1
