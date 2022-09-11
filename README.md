# PROJECT BENIN IMMAT API

## Description

This is the fastapi backend for the Project QUIZREO

To setup 

-- Run `python -m venv py_modules` to create a basic virtual environment

-- Copy content of root file quick_aliases in py_modules/bin/activate

-- Run `source py_modules/bin/activate` to activate the created virtual environment

-- Run `pip install -r requirements.txt` to install the dependancies

-- Be aware of platform specific bugs during the previous step. Solve them until it's alright 😆️

-- Create a .env file at the project's root

-- Copy in the content of .env.example file 

-- Update the .env file according to your database credentials and other variables

-- Run `fastapi:migrations:run` to create tables

-- Run `fastapi:run to start the api server` and voila
