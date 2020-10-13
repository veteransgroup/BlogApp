from .common import *

SECRET_KEY = '2wqrfhw5xa4v$)9=894wmxi^&$hf)8dw#pz)ja0l#5%+u$qcqc'

DEBUG = True

ALLOWED_HOSTS = ['*']

# 搜索设置
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://elasticsearch_local:9200/'
