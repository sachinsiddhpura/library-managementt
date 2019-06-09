from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(models.Model):
    USER_TYPE = (
        ('student','Student'),
        ('faculty','Faculty'),
        ('coordinator','Coordinator')
    )
    name = models.CharField(max_length=120)
    enrolment_number = models.CharField(max_length=120,null=True,blank=True)
    user_type = models.CharField(max_length=120,choices=USER_TYPE)
    semester = models.IntegerField()

    def __str__(self):
        return self.name
