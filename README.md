# bob
[![Build Status](https://semaphoreci.com/api/v1/ahmad88me/bob/branches/master/badge.svg)](https://semaphoreci.com/ahmad88me/bob)


# Prerequisits (one time)
1. [pip](https://pip.pypa.io/en/stable/installing/) 
2. [virtualenv](https://virtualenv.pypa.io/en/latest/)
3. create virtualenv: `virtualenv -p /usr/bin/python2.7 .venv`
4. access the virtualenv: `source .venv/bin/activate`
5. install dependancies: `pip install -r requirements.txt`


# Run
1.  access the virtualenv: `source .venv/bin/activate`
2.  run the web app: `python app.py`
3.  visit `http://127.0.0.1:5000` in your local browser


# Tests
```
python tests/test.py
```
# Coverage: 
```
coverage run --source=. --omit=.venv/*  tests/test.py
coverage report
```
