from django.core.exceptions import PermissionDenied


def authenticate(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
