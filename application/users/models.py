from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=250, unique=True)
    last_name = models.CharField(max_length=250, unique=True)
    phone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)


class UserAddress(models.Model):
    subject = models.CharField(max_length=250, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_address = models.IntegerField()
    coordination = models.IntegerField()
    is_user = models.BooleanField(default=True)
    is_supporter = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.subject)