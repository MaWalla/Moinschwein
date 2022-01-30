from .base import *

ALLOWED_HOSTS = os.getenv('MOINSCHWEIN_ALLOWED_HOSTS', '').split(' ')

STATIC_ROOT = '/app/static'
