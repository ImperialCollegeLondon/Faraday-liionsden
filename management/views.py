from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import NewUserForm

backend = "django.contrib.auth.backends.ModelBackend"


def register_request(request, backend=backend):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, "Registration successful. Your account is pending approval."
            )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request, template_name="registration.html", context={"form": form}
    )


def login_request(request, backend=backend):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user, backend=backend)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(request.GET.get("next", "home"))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request, template_name="login.html", context={"login_form": form}
    )


def logout_request(request):
    logout(request)
    messages.info(request, "you have successfully logged out.")
    return redirect("home")
