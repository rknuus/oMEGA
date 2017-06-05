# oMEGA
prototype of a math exam generator

## Installation / Update
* precondition: requires Python 3
* `pip install -r requirements.txt` (assuming that `pip` is the Python 3 version, else `pip3`)
* apply all migrations with `python manage.py migrate`

## Usage
* to start oMEGA: `python manage.py runserver 8080`
** open URL `localhost:8080/teacher/` in a browser
* to create a teacher: `python manage.py createsuperuser`
* to create, view, edit, or delete exams: open URL `localhost:8080/admin/` in a browser
* to play with the internals: `python manage.py shell`