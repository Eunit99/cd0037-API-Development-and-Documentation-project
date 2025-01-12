# Trivia App

Trivia App was created as an app for the Trivia project based on Udacity course, it has both backend endpoints to handle creation of questions and also returning random question for quizzes. Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out, hence the creation of this trivia API.

It was developed using Flask for backend which follows [PEP8 guidelines](https://peps.python.org/pep-0008/) for python, and ReactJS for the frontend.

## **Getting Started**

You need to have python installed on your machine with Node and NPM (a package manager for node) as the backend uses Python Flask framework and the frontend uses ReactJS.

---

### Backend

---

- Install python if it's not installed from the [official website](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
- create a virtual environment in other to have an isolated system more info [here](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system.)
- change directory to backend, install dependencies using pip

  ```
  pip install -r requirements.txt
  ```
- due to Flask-Cors depreciation some codes have to be corrected from the flask module, open ``core.py`` in ``{path to your env}/python/version/lib/python/site-packages/flask_cors/core.py``

  on **line 322 and 342** change ``collections.Iterable`` to ``collections.abc.Iterable``
- install a relational database management system (rdbms), recommended rdbms is postgresql you can download and get more info [here](https://www.postgresql.org/download/)
- create a database for the backend

  ```
  createdb trivia
  ```
- you can choose to populated the trivia database with sample data provided or by yourself.
  to popluate the database change directory to ``./backend`` and run

  ```
  psql trivia < trivia.psql
  ```
- now to get the flask server running, if you intend to run it in a development environment, export the flask_env and flask_app variables first, change directory to backend

  for window cmd

  ```
  set FLASK_APP=flaskr
  set FLASK_ENV=development
  ```

  for window powershell

  ```
  $Env:FLASK_APP=flaskr
  $Env:FLASK_ENV=development
  ```

  for linux

  ```
  export FLASK_APP=flaskr
  export FLASK_ENV=development
  ```
- you also need to set environment variables for the database user and the database password, the variables are ``DATABASE_USER`` and ``DATABASE_PASS`` respectively.

  for windows more info [here](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html)

  for linux open your ~/.bashrc and add the following line of code to set the variables

  ```
      export DATABASE_USER="yourDatabaseUsername"
      export DATABASE_PASS="yourDatabasePassword"
  ```
- finally run the server with

  ```
   flask run
  ```

---

### Frontend

---

- install nodejs from the official website [here](https://nodejs.dev/)
- install dependencies, change directory to frontend and run

  ```javascript
  npm install
  ```
- this app was created with react which provides a development server, change the script settings in ``package.json`` to your convenience if you are familiar with npm, run the development server with :

  ```
      npm run start
  ```
- a production build can also be created using

  ```
      npm run build
  ```

---

### Tests

---

tests are located in the backend directory in test_flaskr.py file, to run tests:

- change directory to backend
- create a database for the tests

  ```
  createdb trivia_test
  ```

- populate the database with sample data

  ```
  psql trivia_test < trivia.psql
  ```
  
- then run the script with python

  ```
  python test_flaskr.py
  ```

## API Reference

the documentation for the api is in the backend folder, [link here](./backend/README.md)
