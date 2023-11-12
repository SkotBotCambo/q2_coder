# q2_coder

### Working from the following articles
* [How To Build a To-Do application Using Django and React (Digital Ocean Tutorial)](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react#step-3-setting-up-the-frontend)

### Notes
* the version of react-bootstrap used in the tutorial is outdated, some of react bootstrap modals need to be updated to work with modern bootstrap
* There is an issue with modern Node and OpenSSL, need to add `export NODE_OPTIONS=--openssl-legacy-provider
` to the environment to work per this [SO article](https://stackoverflow.com/questions/69692842/error-message-error0308010cdigital-envelope-routinesunsupported)

## `rail_coder`
Django app that helped me code and manage data for the RAIL CSCW workshop data analysis of RAI licenses.
* The app can be found under `/backend/rail_coder/`
* Jupyter notebooks can be run with `pipenv shell`, then `python manage.py shell_plus --lab`
    * `--notebook` doesn't work. Refer to this [GH issue](https://github.com/django-extensions/django-extensions/issues/1835).
* `http://localhost:8000/rail` is the endpoint for this app.