# oMEGA
prototype of a math exam generator

## Installation / Update
* precondition: requires Python 3
* `pip install -r requirements.txt` (assuming that `pip` is the Python 3 version, else `pip3`)
* apply all migrations with `python manage.py migrate`

## User Management
* to create an admin/teacher, which can add, update, and delete exams or create other users: `python manage.py createsuperuser`

## Limitations
* currently variables can be only set to constant values

## Usage
* to start oMEGA: `python manage.py runserver 8080`
  * open URL `localhost:8080/teacher/` in a browser
* to create, view, edit, or delete exams: open URL `localhost:8080/admin/` in a browser and login as admin/teacher (see section User Management)
  * as example create a new exam and enter the following values:
    * set 'Variables:' to '{ "X":0, "Y":42 }'
    * set 'Content:' to '{X} + {Y} = ?'
  * save the changes and open the exam under `localhost:8080/teacher/`, the variables in the content should get replaced by the constants
* to play with the internals: `python manage.py shell`

## To Do
* add data model element Question and let Exams contain 0..N Questions, per Question can define variables, result (may be predefined name, but customizable constraints), and template text referencing variables and result