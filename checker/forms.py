from checker.status import http_status_list
from .models import Site

from django.forms import ModelForm, MultipleChoiceField


class SiteForm(ModelForm):
    status_code_list = list(map(lambda status: status["code"], http_status_list))
    status_list = MultipleChoiceField(choices=status_code_list, required=True)

    class Meta:
        model = Site
        fields = ["owner", "name", "url", "status_list"]
