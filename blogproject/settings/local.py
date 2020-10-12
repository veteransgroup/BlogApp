from .common import *

SECRET_KEY = 'ynx!of6i^l)fg4mrxq-151b&q^kn%4c!26v=-0+zzg1l)=g&e)'

DEBUG = True

ALLOWED_HOSTS = ['*']

# 搜索设置
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://elasticsearch_local:9200/'
