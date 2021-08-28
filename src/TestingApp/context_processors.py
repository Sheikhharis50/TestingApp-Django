from django.conf import settings


def globals(request):
    return {
        'PROTOCOL': settings.PROTOCOL,
        'PAGE_SIZE': settings.PAGE_SIZE,
        'APP_NAME': settings.APP_NAME,
        'NAV_ITEMS': navigations()
    }


def navigations():
    return [
        {
            'label': 'Home',
            'path': '/',
        },
        {
            'label': 'About',
            'path': '/about'
        },
        {
            'label': 'Questions',
            'path': '/questions'
        },
        {
            'label': 'Orders',
            'path': '/orders'
        },
        {
            'label': 'EMS',
            'path': '/ems'
        }
    ]
