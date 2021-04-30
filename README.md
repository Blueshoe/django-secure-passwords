![django-secure-passwords logo](https://github.com/Blueshoe/django-secure-passwords/raw/master/docs/_static/img/logo.png)

--------------------------------------------------------------------------------
![Build Status](https://github.com/Blueshoe/django-secure-passwords/actions/workflows/python-app.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Blueshoe_django-secure-passwords&metric=alert_status)](https://sonarcloud.io/dashboard?id=Blueshoe_django-secure-passwords)
[![Coverage Status](https://coveralls.io/repos/github/Blueshoe/django-secure-passwords/badge.svg?branch=master)](https://coveralls.io/github/Blueshoe/django-secure-passwords?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


**Todo**


## Installation

django-secure-passwords is currently available only on Blueshoe's Python Package Index.
```bash
pip3 install django-secure-passwords
```

Add *"django-secure-passwords"* to your *INSTALLED_APPS*: 
```python
INSTALLED_APPS = [
    "...",
    "securepasswords",
]
```



## Tracking of login attempts and account blocking
To track login attempts and lock account after a number of unsuccessful attempts use 
[django-axes](https://github.com/jazzband/django-axes/) package. It can log successful and unsuccessful attempts, saving 
this information to the database. The record consists of time of login, IP address, user 
agent, username, path to which the login was attempted and the number of failed attempts.

To install this package, run:
```bash
pip3 install django-axes
```

Then, according to the [installation guide](https://django-axes.readthedocs.io/en/latest/2_installation.html) you need
to add these settings to your settings.py file:

```python
INSTALLED_APPS = [
    '...',
    # Axes app can be in any position in the INSTALLED_APPS list.
    'axes',
]
```

```python
AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',
    '...',
]
```

```python
MIDDLEWARE = [
    # The following is the list of default middleware in new Django projects.
    '...',
    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    # It only formats user lockout messages and renders Axes lockout responses
    # on failed user authentication attempts from login views.
    # If you do not want Axes to override the authentication response
    # you can skip installing the middleware and use your own views.
    'axes.middleware.AxesMiddleware',
]
```

Different [configuration variables](https://django-axes.readthedocs.io/en/latest/4_configuration.html) are available, 
those variables can be directly added to the settings.py file.

## Usage

# TODO prettify
Recommended: usage of `AbstractBaseUser` subclass as `AUTH_USER_MODEL`

