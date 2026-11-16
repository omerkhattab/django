from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    duty = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name