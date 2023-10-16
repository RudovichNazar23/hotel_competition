from django.shortcuts import render


class CheckUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return render(request, "registration_app/registration_form.html")
        else:
            return render(request, "admin_app/home.html")
