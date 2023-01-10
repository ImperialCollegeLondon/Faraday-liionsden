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
        form.instance.user_owner = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            # Do other stuff before saving here
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
    inline_formsets should be of the form {"inline_formset_name": formset_class}.
    """

    success_message = "New data added successfully."
    failure_message = "Cannot add data. Invalid information."
    success_url = None
    inline_formsets = {}  # Dictionary of inline formsets to be added to context

    def get_context_data(self, **kwargs):
        """
        Helper function to get correct context to pass to render() in get()
        and post().
        """
        data = super(NewDataViewInline, self).get_context_data(**kwargs)
        if self.request.POST:
            for key, formset in self.inline_formsets.items():
                data[key] = formset(self.request.POST, self.request.FILES)
        else:
            for key, formset in self.inline_formsets.items():
                data[key] = formset()
        return data

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        form.instance.user_owner = request.user
        context = self.get_context_data()
        context["form"] = form  # update form in context for form errors in render
        if form.is_valid():
            # Save instance incluing setting user owner and status
            with transaction.atomic():
                obj = form.save(commit=False)
                if form.is_public():
                    obj.status = "public"
                else:
                    obj.status = "private"
                self.object = form.save()
            # Save individual parameters from inline forms
            formsets_valid = True
            for key in self.inline_formsets.keys():
                formset = context[key]
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()
                else:
                    self.object.delete()
                    formsets_valid = False
                    break
            # If all inline forms are valid, save instance and redirect
            if formsets_valid:
                messages.success(request, self.success_message)
                # Redirect to object detail view or stay on form if "add another"
                if "another" in request.POST:
                    return redirect(request.path_info)
                else:
                    return (
                        redirect(self.success_url)
                        if self.success_url
                        else redirect(obj)
                    )
        # If form or a formset is not valid, render form with errors
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
    inline_formsets should be of the form {"inline_formset_name": formset_class}.
    """

    success_message = "New data added successfully."
    failure_message = "Cannot add data. Invalid information."
    inline_formsets = {}

    def get_context_data(self, **kwargs):
        """
        Helper function to get correct context to pass to render() in get()
        and post().
        """
        data = super(UpdateDataInlineView, self).get_context_data(**kwargs)
        if self.request.POST:
            for key, formset in self.inline_formsets.items():
                data[key] = formset(self.request.POST, instance=self.object)
        else:
            for key, formset in self.inline_formsets.items():
                data[key] = formset(instance=self.object)
        return data

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data()
        if form.is_valid():
            # Save experiment incluing setting user owner and status
            with transaction.atomic():
                if form.is_public():
                    self.object.status = "public"
                else:
                    self.object.status = "private"
                self.object.save()
            # Save individual parameters from inline form
            formsets_valid = True
            for key in self.inline_formsets.keys():
                formset = context[key]
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()
                else:
                    formsets_valid = False
                    break
            # If all inline forms are valid, save instance and redirect
            if formsets_valid:
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
        # If form or a formset is not valid, render form with errors
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
