from django.db import models

from model_utils.models import TimeStampedModel

from pingdumb.users.models import User


class Site(TimeStampedModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    url = models.CharField(max_length=65536)
