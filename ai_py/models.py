from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)

class Contact(models.Model):
    code = models.CharField("code", max_length=255, blank = True, null = True)
    name = models.CharField("name", max_length=255, blank = True, null = True)
    # phone = models.CharField(max_length=20, blank = True, null = True)
    # address = models.TextField(blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    # createdAt = models.DateTimeField("Created At", auto_now_add=True)
