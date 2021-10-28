import json
from dateutil.parser import parse
import pytz
from django.core import exceptions
from django.conf import settings
import logging
from datetime import datetime
import string
import random


def extractBody(request, POST=False):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except:
        data = request.POST if POST else request.GET

    return data


def get_model_fields(model):
    return [f.name for f in model._meta.get_fields()]


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


def getPageData(pno, psize, data_list):
    psize = settings.PAGE_SIZE if not psize else int(psize)
    offset = psize * int(pno)
    return data_list[offset: offset+psize], True if offset+psize < len(data_list) else False


def getCleanData(obj, list=[]):
    data = {}
    for key in list:
        data[key] = obj.cleaned_data.get(key)
    return data


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


def pw_gen(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def _gen_salt():
    _now = datetime.now()
    return (_now.year - 2000) * 1209000 + (_now.month * 93000) \
        + (_now.day * 2905) + (_now.hour * 121) + (_now.minute * 2)
