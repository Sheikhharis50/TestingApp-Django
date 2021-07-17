import json
from dateutil.parser import parse
import pytz
from django.core import exceptions


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
