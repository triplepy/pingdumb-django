from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from checker.forms import SiteForm


class SiteFormView(LoginRequiredMixin, FormView):
    form_class = SiteForm
    context_object_name = 'site'
    template_name = 'checker/site_form.html'
