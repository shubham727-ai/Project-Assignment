from django.db import models

# Create your models here.

makemigration - create change and store in a file
migrate - apply the pending change created by makemigrations


class index(models.model):
    name =models.models.CharField(_(""), max_length=50)
    surname =models.models.CharField(_(""), max_length=50)
    age =models.models.CharField(_(""), max_length=50)
    skills =models.models.CharField()
    desc =models.models.TextField(_(""), max_length=50)

