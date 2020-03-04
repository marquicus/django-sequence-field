SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
    "sequence_field",
]
USE_TZ = True
TIME_ZONE = 'UTC'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}
