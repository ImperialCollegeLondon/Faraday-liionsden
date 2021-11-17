from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import NewUserForm


def register_request(request, backend="django.contrib.auth.backends.ModelBackend"):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful.")
            return redirect("battDB:Experiments")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request, template_name="registration.html", context={"form": form}
    )
