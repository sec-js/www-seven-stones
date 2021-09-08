from structlog.stdlib import _FixedFindCallerLogger
import logging.handlers
import logging.config
import inspect
import datetime
import pytz
from structlog import configure, processors, stdlib, threadlocal
from structlog import wrap_logger
from structlog.processors import JSONRenderer
from sevenstones.settings import BASE_DIR

def log_crunch():

    APP_LOG = BASE_DIR + "/logs/debug.json"
    DJANGO_CRASH_LOG = BASE_DIR + "/logs/crash.log"

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
                    'require_debug_false': {
                        '()': 'django.utils.log.RequireDebugFalse'
                     }
        },
        'formatters': {
            'json': {
                # 'format': '%(name)s; %(levelname)s; %(module)s; %(message)s; %(lineno)d; %(pathname)s',
                # 'format': '%(message)s; %(function_name)s; %(file_name)s; %(line_number)s',
                'format': '%(message)s;'
                # 'format': '%(message)s; %(stack)s',
                #'()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            },
        },
        'handlers': {
            'json_app': {
                'class': 'logging.FileHandler',
                'filename': APP_LOG,
                'formatter': 'json',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
            # Log to a text file that can be rotated by logrotate
            'crash_logfile': {
                # 'class': 'logging.FileHandler',
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': DJANGO_CRASH_LOG,
            },
        },
        'loggers': {
            'seven_app': {
                'handlers': ['json_app'],
                'level': logging.INFO
            },
            'django.request': {
                'handlers': ['json_app'],
                'level': 'WARN',
                'propagate': False,
            },
            '': {
                'handlers': ['crash_logfile'],
                'level': 'WARN',
                'propagate': False,
            },
        }
    })


    # logging.basicConfig(stream=sys.stdout, format='%(message)s')

    def add_stack_info(_, __, event_dict):

        frame = inspect.stack()[3]
        # (file_name, line_number,
        #  function_name, lines, index) = inspect.getframeinfo(frame)

        event_dict['file_name'] = frame[1]
        event_dict['line_number'] = frame[2]
        event_dict['function_name'] = frame[3]

        return event_dict

    def add_timestamp(_, __, event_dict):

        now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

        event_dict['timestamp'] = now

        return event_dict

    log_app = wrap_logger(
        logging.getLogger('seven_app'),
        processors=[
            #stdlib.add_logger_name,
            stdlib.add_log_level,
            stdlib.filter_by_level,
            add_stack_info,
            add_timestamp,
            JSONRenderer(indent=2, sort_keys=False),
        ],
    )

    return log_app


# logger_debug = structlog.getLogger('netdelta_debug')
# logger_app = structlog.getLogger('netdelta_app')

#
# def logsmash(logger, level, message, **kwargs):
#
#     previous_frame = inspect.currentframe().f_back
#     (filename, line_number,
#      function_name, lines, index) = inspect.getframeinfo(previous_frame)
#     #        return (filename, line_number, function_name, lines, index)
#
#     print filename, line_number, function_name
#
#     print("logger is {0}, message is {1}, and kwargs {2}").format(logger, message, kwargs)