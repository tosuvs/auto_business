from django.db import models


class DateAddedUpdatedAvailable(models.Model):
    is_available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DateAdded(models.Model):
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DateUpdatedAdded(models.Model):
    added_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
