"""Application logging for devwrangler."""
import logging
import os
from logging.config import dictConfig

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {'format': '%(message)s'},
    },
    'filters': {},
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': "rich.logging.RichHandler",
            'rich_tracebacks': True,
            'markup': True,
            'tracebacks_show_locals': True,
        },
    },
    'loggers': {
        'devwrangler': {
            'handlers': ['console'],
            'propagate': True,
            'level': os.environ.setdefault("DW_LOG_LEVEL", "WARNING"),
        },
    },
}

LOG = logging.getLogger('devwrangler')
dictConfig(LOGGING)
