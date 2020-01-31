from django.http import HttpResponseRedirect


def unauthenticated_only(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return _wrapped_view_func
