# Herbal Antidote

Herbal Antidote is a wellness app. It's a quiz that takes you through a series of true/false questions, and used that information to generate recommendations for herbal remedies based on the needs of the user. It uses GoogleMaps API for geolocation servies, allowing the user to search for local herb shops in the area. 


## About

### Features

* Bootstrap 4

* Heroku support

* Pipenv: It's set-up to use Pipfile

* Misc nice stuff:
    * `django-debug-toolbar` -- great debugging tool
    * Error pages

### Backend

* Python/Django

### Database
* SQLite database was used for local development. 
* Pushing app to Heroku requires use of Postgres database. 

## Development

* Prereq: [You have Pipenv installed.
  ](https://github.com/kickstartcoding/pipenv-getting-started) You have Django
  admin installed globally (macOS type `pip3 install django`, Ubuntu GNU/Linux,
  type `sudo pip3 install django`)

### Running locally


2. Go into the newly created project, and use `pipenv` to get your virtualenv
setup
```
cd mycoolproject
pipenv shell
pipenv install --dev
```

5. Get the server running:
```
python manage.py runserver
```


### File structure

Directory structure description below:

```python
[name_of_project]/
    - config/
        - base.py          # Stores most settings
        - local.py         # Stores settings only for local dev
        - production.py    # Stores settings only used by production (e.g. Heroku)
    - urls.py              # Global urls.py, in turn includes urls.py in apps

- apps/                    # A directory to store all our custom apps
    - accounts/            # An example custom app that includes sign-up and log-in
        - models.py        # Customized user class is here
        - urls.py          # URLs for sign-up and log-in pages
        - views.py         # Views for sign-up and log-in pages
        - forms.py         # Form for editing user profile, sign-up
        - templates/       # Templates for user profile stuff
    - core/                # An example custom app that has some static pages
        - static/          # Static files
        - templates/       # Core templates, including base templates
        - etc
- manage.py                # Entry point
- Pipfile                  # Development requirements
```


## Production


### Provisioning on Heroku

1. Creating a new Heroku app & Postgres Database (only need to do this once per
Heroku):
```bash
heroku create # Create a Heroku app (only run this if you haven't already)
heroku addons:create heroku-postgresql:hobby-dev
```

2. *Optional:* Confirm that the database is working by connecting to it with the
command-line client (`Ctrl+D` to exit):
```bash
heroku pg:psql
```

3. Push to Heroku
```bash
git push heroku master
```


5. Run the migrations on the remote Postgres database. That can be done as
follows:
```bash
heroku run python manage.py migrate
```

6. Your site should work! View it in your browser.

7. You'll also want to add a `SECRET_KEY` to Heroku to make your site secure:
```bash
heroku config:set SECRET_KEY=randomly hit keys
```

NOTE: Where it says "randomly hit keys", do just that!  Just type a really long
random series of letters and numbers. You'll never have to remember it again.

----------------------

