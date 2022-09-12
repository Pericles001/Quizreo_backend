# Quizreo_backend
Backend application for quizreo application : API and services are stored there


![question mark](https://th.bing.com/th/id/R.0eb9d2f7d65c0b155094266709c3dcda?rik=jy9Drj8zZOjYZg&pid=ImgRaw&r=0)


## Description

This application is the backend of the quizreo application. It is a REST API that provides services to the quizreo application. It is written in python with fastAPI framework.

###  Technologies

* [python](https://www.python.org/)
* [fastAPI](https://fastapi.tiangolo.com/)
* [postgresql](https://www.postgresql.org/)

### Architecture

The application is divided into 6 parts:

```
*      [app](app/): contains the main application
*           [auth](app/auth/): contains the authentication services
*           [core](app/core/): contains the core services
*           [database](app/db/): contains the database services
*           [endpoints](app/endpoints/): contains the endpoints of the API
*           [models](app/models/): contains the models of the database
*           [routes](app/routes/): contains the routes of the API
*      __init__.py
*      dependencies.py
*      main.py
*      test_main.py
``` 

###  Services

Services provided by the API:
* Authentication : login, logout, register, reset password, change password
* User management : get user, update user, delete user
* Quiz management : create quiz, get quiz, update quiz, delete quiz
* Survey management : create survey, get survey, update survey, delete survey 
* Answer management : create answer, get answer, update answer, delete answer
* Party management : create party, get party, update party, delete party
* Trial management : create trial, get trial, update trial, delete trial


###  API


####  Authentication

* [login](app/endpoints/auth/login.py): login a user
* [logout](app/endpoints/auth/logout.py): logout a user
* [register](app/endpoints/auth/register.py): register a user
* [reset_password](app/endpoints/auth/reset_password.py): reset the password of a user

####  User
* [get_user](app/endpoints/user.py): get a user
* [update_user](app/endpoints/user.py): update a user
* [delete_user](app/endpoints/user.py): delete a user
* [get_users](app/endpoints/user.py): get all users
* [get_user_by_username](app/endpoints/user.py): get a user by username

####  Quiz
* [create_quiz](app/endpoints/quiz.py): create a quiz
* [get_quiz](app/endpoints/quiz.py): get a quiz
* [update_quiz](app/endpoints/quiz.py): update a quiz
* [delete_quiz](app/endpoints/quiz.py): delete a quiz
* [get_quizzes](app/endpoints/quiz.py): get all quizzes
* [get_quiz_by_name](app/endpoints/quiz.py): get a quiz by name
* [get_quiz_by_user](app/endpoints/quiz.py): get all quizzes of a user

####  Survey
* [create_survey](app/endpoints/survey.py): create a survey
* [get_survey](app/endpoints/survey.py): get a survey
* [update_survey](app/endpoints/survey.py): update a survey
* [delete_survey](app/endpoints/survey.py): delete a survey
* [get_surveys](app/endpoints/survey.py): get all surveys
* [get_survey_by_name](app/endpoints/survey.py): get a survey by name
* [get_survey_by_user](app/endpoints/survey.py): get all surveys of a user

####  Answer
* [create_answer](app/endpoints/answer.py): create an answer
* [get_answer](app/endpoints/answer.py): get an answer
* [update_answer](app/endpoints/answer.py): update an answer
* [delete_answer](app/endpoints/answer.py): delete an answer
* [get_answers](app/endpoints/answer.py): get all answers
* [get_answer_by_user](app/endpoints/answer.py): get all answers of a user
* [get_answer_by_quiz](app/endpoints/answer.py): get all answers of a quiz

####  Party
* [create_party](app/endpoints/party.py): create a party
* [get_party](app/endpoints/party.py): get a party
* [update_party](app/endpoints/party.py): update a party
* [delete_party](app/endpoints/party.py): delete a party
* [get_parties](app/endpoints/party.py): get all parties
* [get_party_by_name](app/endpoints/party.py): get a party by name
* [get_party_by_user](app/endpoints/party.py): get all parties of a user

### Trial
* [create_trial](app/endpoints/trial.py): create a trial
* [get_trial](app/endpoints/trial.py): get a trial
* [update_trial](app/endpoints/trial.py): update a trial
* [delete_trial](app/endpoints/trial.py): delete a trial
* [get_trials](app/endpoints/trial.py): get all trials
* [get_trial_by_name](app/endpoints/trial.py): get a trial by name
* [get_trial_by_user](app/endpoints/trial.py): get all trials of a user

## Usage

If you want to use this project as a template, you can clone it and start working on it. You can also use it as a reference to learn how to build a FastAPI project.
If you want to see a demo of the various features follow these steps: 

1. Clone the project

*      git clone https://github.com/Pericles001/Quizreo_backend.git
*      cd Quizreo_backend

2. Create a virtual environment

*      python3 -m venv venv
*      source venv/bin/activate

3. Install the requirements

*     pip install -r requirements.txt
*     pip install -r requirements-dev.txt

4. Run the project

*     uvicorn app.main:app --reload

5. Go to the [Swagger UI](http://localhost:8000/docs) and try the endpoints
6. Go to the [ReDoc UI](http://localhost:8000/redoc) and try the endpoints


## Contributing

If you wish to contribute to the application , you can fork the project and submit a pull request. If you find any bugs or have any suggestions, you can open an issue.


## Authors

* [Pericles001](https://github.com/Pericles001)