from django.db import models

# Create your models here.


class contents(models.Model):
    subject = models.CharField(_(""), max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField()
