# -*- coding: utf-8 -*-
"""
    pynotebook.settings
    ~~~~~~~~~~~~~~~~~~~

    pynotebook settings module
"""

DEBUG = True

SECRET_KEY = 'pynotebook-secret-key'
CSRF_ENABLED = True

SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/pynotebook'
CELERY_BROKER_URL = 'redis://localhost/0'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'}
]
