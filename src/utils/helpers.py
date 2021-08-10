import json
from dateutil.parser import parse
import pytz
from django.core import exceptions
from django.conf import settings
import logging
from datetime import datetime


def extractBody(request):
    body_unicode = request.body.decode('utf-8')
    return json.loads(body_unicode)


def get_model_fields(model):
    return model._meta.fields


def parse_dt_str(datetime_str):
    date_with_offset = parse(datetime_str)
    try:
        utc_date = pytz.utc.localize(date_with_offset)
    except ValueError:
        raise ValueError(
            'Date `{0}` missing timezone information, please provide'
            ' valid date. \nExpected format: YYYYMMDDHHMM+HHMM or'
            ' YYYYMMDDHHMM-HHMM i.e: 201801012230-0500'
            ' (Jan-01-18 10:30pm EST)'.format(datetime_str))

    return utc_date


def ObjectsListToJSON(objs_list):
    def objToJson(obj):
        return obj.values()
    return list(map(objToJson, objs_list))


def SelectFromObj(objs_list, *args):
    def includes(obj):
        data = {}
        for arg in args:
            data[arg] = obj[arg] if arg in obj else None
        return data
    return list(map(includes, objs_list))


def getPageData(pno, data_list):
    offset = settings.PAGE_SIZE * int(pno)
    return data_list[offset: offset+settings.PAGE_SIZE]


def log(message, level="error"):
    loggers = {
        'error': logging.error,
        'warn': logging.warning,
        'info': logging.info,
        'debug': logging.debug,
        'critical': logging.critical,
    }
    loggers[level](
        "[%s][%s]: %s" %
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            str(level).upper(), str(message)
        )
    )


def getSiteURL(request):
    return "{}://{}/".format(settings.PROTOCOL, request.META['HTTP_HOST'])
