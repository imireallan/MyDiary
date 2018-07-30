https://travis-ci.org/imireallan/MyDiary.svg?branch=ch-api-v2-enpoints-159268511
[![Coverage Status](https://coveralls.io/repos/github/imireallan/MyDiary/badge.svg)](https://coveralls.io/github/imireallan/MyDiary)

# MyDiary
MyDiary is an online journal where users can pen down their thoughts and feelings.

## Requirements
Have the following set up on your local environment before getting started

1. [python 3.x](https://www.python.org/downloads/)
2. [Git](https://git-scm.com)
3. Working browser or [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?utm_source=chrome-app-launcher-info-dialog)
4. [Postgres](http://www.postgresql.org)

## Installation
For the UI designs to work you need a working browser like google chrome or mozilla firefox

Clone the repository into your local environment

```
git clone git@github.com:imireallan/MyDiary.git
```

Change directory into MyDiary

```
cd MyDiary/UI
```

Run `index.html` file in your browser

UI link for gh-pages

```
https://imireallan.github.io/MyDiary/UI/index.html
```

## API Installation
To set up MyDiary API, make sure that you have python3, postman and pip installed.

Use [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) for an isolated working environment.

Clone the Repo into a folder of your choice
```
git clone https://github.com/imireallan/MyDiary.git
```

Create a virtual enviroment.
```
virtualenv venv --python=python3
```

Navigate to api folder.
```
cd MyDiary
```

Install the packages.
```
pip3 install -r requirements.txt
```

Set environment variables for `SECRET`,`FLASK_CONFIG`
> `SECRET` is your secret key

> `FLASK_CONFIG` is the enviroment you are running on. Should be either `Production`, `Development` or `Testing`. NOTE: its case sensitive


## API Usage

To get the app running...

```bash
$ python manage.py run
```

Open root path in your browser to test the endpoints. 
You can also use Postman or any other agent to test the endpoints

## Test

To run your tests use

```bash
$ python manage.py test
```

To test endpoints manually fire up postman and run the following endpoints

**EndPoint** | **Functionality**
--- | ---
GET  `/api/v2/entries` | Fetch all entries
GET  `/api/v2/entries/<entryId>` | Fetch a single entry 
POST  `/api/v2/entries` | Create an entry
PUT  `/api/v2/entries/<entryId>` | Modify an entry
DELETE  `/api/v2/entries/<entryId>` | Delete an entry
POST  `/api/v2/auth/signup` | Register a user
POST  `/api/v2/auth/login` | Logs in a user



# API Documentation
Once app server is running you can view API documentation from
```
http://127.0.0.1:5000/api/documentation
```
