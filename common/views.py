from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render  # noqa: F401
from django.views.generic.edit import DeleteView, FormView, UpdateView


class NewDataView(FormView):
    """
    Template for view for creating new entries of various models.
    """

    success_message = "New data added successfully."
    failure_message = "Cannot add data. Invalid information."
    success_url = None

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            # Do other stuff before saving here
            obj.user_owner = request.user
            if form.is_public():
                obj.status = "public"
            else:
                obj.status = "private"
            obj.save()
            messages.success(request, self.success_message)
            # Redirect to object detail view or stay on form if "add another"
            if "another" in request.POST:
                return redirect(request.path_info)
            else:
                return redirect(self.success_url) if self.success_url else redirect(obj)
        messages.error(request, self.failure_message)
        return render(request, self.template_name, {"form": form})


class NewDataViewInline(FormView):
    """
    Template for view for creating entries that includes an inline
    form for e.g. adding child objects, related objects etc.
    """

    success_message = "New data added successfully."
    failure_message = "Cannot add data. Invalid information."
    success_url = None
    inline_key = None  # Key for which an inline form is needed
    formset = None  # Formset specifying the fields in the inline form

    def get_context_data(self, **kwargs):
        """
        Helper function to get correct context to pass to render() in get()
        and post().
        """
        data = super(NewDataViewInline, self).get_context_data(**kwargs)
        if self.request.POST:
            data[self.inline_key] = self.formset(self.request.POST, self.request.FILES)
        else:
            data[self.inline_key] = self.formset()
        return data

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = self.get_context_data()
        parameters = context[self.inline_key]
        if form.is_valid():
            # Save instance incluing setting user owner and status
            with transaction.atomic():
                obj = form.save(commit=False)
                obj.user_owner = request.user
                if form.is_public():
                    obj.status = "public"
                else:
                    obj.status = "private"
                self.object = form.save()
            # Save individual parameters from inline form
            if parameters.is_valid():
                parameters.instance = self.object
                parameters.save()
            messages.success(request, self.success_message)
            # Redirect to object detail view or stay on form if "add another"
            if "another" in request.POST:
                return redirect(request.path_info)
            else:
                return redirect(self.success_url) if self.success_url else redirect(obj)
        messages.error(request, self.failure_message)
        return render(request, self.template_name, context)


class UpdateDataView(UpdateView):
    success_message = "Entry updated successfully."
    failure_message = "Could not update entry. Invalid information."

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            # Do other stuff before saving here
            if form.is_public():
                self.object.status = "public"
            else:
                self.object.status = "private"
            self.object.save()
            messages.success(request, self.success_message)
            # Redirect to object detail view or stay on form if "add another"
            if "another" in request.POST:
                return redirect(request.path_info)
            else:
                return (
                    redirect(self.success_url)
                    if self.success_url
                    else redirect(self.object)
                )
        messages.error(request, self.failure_message)
        return render(request, self.template_name, {"form": form})


class UpdateDataInlineView(UpdateView):
    """
    Template for view for updating entries that includes an inline
    form for e.g. adding child objects, related objects etc.
    """

    success_message = "New data added successfully."
    failure_message = "Cannot add data. Invalid information."
    inline_key = None  # Key for which an inline form is needed
    formset = None  # Formset specifying the fields in the inline form

    def get_context_data(self, **kwargs):
        """
        Helper function to get correct context to pass to render() in get()
        and post().
        """
        data = super(UpdateDataInlineView, self).get_context_data(**kwargs)
        if self.request.POST:
            data[self.inline_key] = self.formset(
                self.request.POST, instance=self.object
            )
        else:
            data[self.inline_key] = self.formset(instance=self.object)

        return data

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data()
        parameters = context[self.inline_key]
        if form.is_valid():
            # Save experiment incluing setting user owner and status
            with transaction.atomic():
                if form.is_public():
                    self.object.status = "public"
                else:
                    self.object.status = "private"
                self.object.save()
            # Save individual parameters from inline form
            if parameters.is_valid():
                parameters.instance = self.object
                parameters.save()
            messages.success(request, self.success_message)
            # Redirect to object detail view or stay on form if "add another"
            if "another" in request.POST:
                return redirect(request.path_info)
            else:
                return (
                    redirect(self.success_url)
                    if self.success_url
                    else redirect(self.object)
                )
        messages.error(request, self.failure_message)
        return render(request, self.template_name, context)


class MarkAsDeletedView(DeleteView):
    """Custom delete view that does not actually delete the object
    but marks its status as deleted.
    """

    success_message = "Object deleted."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = "deleted"
        self.object.save()
        messages.success(request, self.success_message)
        return redirect(self.success_url)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
