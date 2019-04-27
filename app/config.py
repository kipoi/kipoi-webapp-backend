"""
App configuration file
"""

DEBUG = True

# Cache config
CACHE_TYPE = 'simple'
MEMCACHED_SERVERS = ['127.0.0.1:11221']
CACHE_TIMEOUT = 600  # Cache duration in seconds

SOURCE = 'kipoi'
