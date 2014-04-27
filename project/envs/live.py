import os
from memcacheify import memcacheify
from postgresify import postgresify
from envs.common import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django_ses.SESBackend'
BROKER_URL = os.environ["REDISTOGO_URL"]

MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = '%sadmin/' % STATIC_URL
COMPRESS_URL = STATIC_URL
FAVICON_URL = "%sfavicon.ico" % STATIC_URL

CACHES = memcacheify()
DATABASES = None
DATABASES = postgresify()
NEO4J_URL = os.environ["GRAPHENEDB_URL"]

# Ugh.  Someone has to have solved this *much* better
NEO4J_USER = NEO4J_URL.split("//")[1].split(":")[0]
NEO4J_PASSWORD = NEO4J_URL.split("//")[1].split(":")[1].split("@")
NEO4J_HOST = NEO4J_URL.split("@")[1].split(":")[0]
NEO4J_PORT = NEO4J_URL.split("@")[1].split(":")[1]

NEO4J_DATABASES = {
    'default': {
        'HOST': NEO4J_HOST,
        'PORT': NEO4J_PORT,
        'ENDPOINT': '/',
        'USER': NEO4J_USER,
        'PASSWORD': NEO4J_PASSWORD,
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = "backends.CachedS3BotoStorage"
COMPRESS_STORAGE = STATICFILES_STORAGE

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
GOOGLE_ANALYTICS_PROPERTY_ID = "UA-47030017-1"
