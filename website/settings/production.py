from .defaults import *

DEBUG = False
TEMPLATE_DEBUG = False

urlparse.uses_netloc.append('postgres')
urlparse.uses_netloc.append('mysql')
try:
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    DATABASES = {}
    DATABASES['default'] = {
        'NAME':     url.path[1:],
        'USER':     url.username,
        'PASSWORD': url.password,
        'HOST':     url.hostname,
        'PORT':     url.port,
    }
    if url.scheme == 'postgres':
        DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    if url.scheme == 'mysql':
        DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except:
    print "Unexpected error:", sys.exc_info()