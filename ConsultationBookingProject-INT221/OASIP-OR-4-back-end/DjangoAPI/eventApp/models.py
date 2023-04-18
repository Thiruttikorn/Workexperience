
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Events(models.Model):
    Booking_id = models.AutoField(primary_key=True)
    Booking_name = models.CharField(max_length=100,null=False)
    Booking_email = models.CharField(max_length=100)
    Event_startTime = models.DateTimeField()
    Event_endTime = models.DateTimeField()
    Event_notes = models.CharField(null=True, max_length=500,blank=True)
    Event_category = models.ForeignKey(
        'Categorys', on_delete=models.CASCADE,editable=False)


class Categorys(models.Model):
    Event_category_id = models.AutoField(primary_key=True)
    Event_category_name = models.CharField(max_length=100)
    Event_category_description = models.CharField(max_length=500,blank=True,null=True)
    Event_duration = models.IntegerField()

class Users(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'Admin', _('Admin')
        LECTURER ='Lecturer', _('Lecturer')
        STUDENT = 'Student', _('Student')

    REQUIRED_FIELDS = ('role',)

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,null=False, unique=True)
    email = models.CharField(max_length=50,null=False, unique=True)
    password = models.CharField(max_length=100,null=False)
    role = models.CharField(max_length=20,
        choices=Roles.choices,
        default=Roles.STUDENT)
    createdOn = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updatedOn = models.DateTimeField(auto_now=True,null=True,blank=True)

class Event_category_owner(models.Model):
    Event_category_owner_id = models.AutoField(primary_key=True)
    Event_category_owner_user_id = models.ForeignKey(
        'Users', on_delete=models.CASCADE,editable=False, null=False)
    Event_category_owner_category_id = models.ForeignKey(
        'Categorys', on_delete=models.CASCADE,editable=False)