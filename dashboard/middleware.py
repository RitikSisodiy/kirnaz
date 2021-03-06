from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.shortcuts import redirect, render
from django.urls import resolve
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        r = resolve(request.path)
        if r._func_path[:r._func_path.find('.')] in ["dashboard"]: #add app name IN LIST  to APPLY middleware in that app
            if request.user.is_superuser:
                response = get_response(request)
            else:
                response = render(request,'logindashboard.html')
        else:
            response = get_response(request)
        return response
    return middleware