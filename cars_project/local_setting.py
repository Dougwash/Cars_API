# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x)!jpokenngm*7$ev#z2(teu37e4vu0+waakzq0r_gc)@kk&+s'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Samsung',
    },
}
