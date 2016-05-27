import os

HOST = os.environ.get('THOST', '127.0.0.1')


from django.conf import settings

settings.configure(
    ADMINS=('test', 'test@test.com'),

    APPEND_SLASH=False,

    ALLOWED_HOSTS=('33.33.33.8', 'localhost', 'test.me'),

    ROOT_URLCONF='views',

    DATABASES={
        'default': {
            'ENGINE': 'django_postgrespool',
            'HOST': HOST,
            'NAME': 'test',
            'USER': 'test',
            'PASSWORD': 'test',
            'TEST_CHARSET': 'utf8',
        }
    },
    DATABASE_POOL_ARGS={
        'max_overflow': 10,
        'pool_size': 10,
    },
    CACHE_BACKEND='locmem://',

    TEMPLATE_DIRS=(os.path.dirname(os.path.abspath(__file__)),),

    INSTALLED_APPS=(),

    TEMPLATE_CONTEXT_PROCESSORS=(
        'django.core.context_processors.static',
        'django.core.context_processors.request',
    ),

    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
)

from django.apps import apps
apps.populate(settings.INSTALLED_APPS)

from django.core.handlers.wsgi import WSGIHandler
app = WSGIHandler()
