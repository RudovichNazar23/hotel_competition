from django.shortcuts import redirect


class CheckUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect(to="registration/form")
        else:
            return redirect(to="administrator/home")
