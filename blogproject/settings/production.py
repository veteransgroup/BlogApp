from .common import *

SECRET_KEY = '8k@0h5kklahg9!650a6jdsx80on6no$hwtsnawqxt0&4macd7h'                 # os.environ['DJANGO_SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['*']
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://elasticsearch:9200/'
