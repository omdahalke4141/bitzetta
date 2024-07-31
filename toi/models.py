from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def validate_mobile_number(value):
    if not value.isdigit():
        raise ValidationError("Mobile number should contain only digits.")
    if not len(value)==10:
        raise ValidationError("Mobile number should contain only 10 digits.")


USER_CHOICES = [
    ('user','user'),
    ('admin','admin'),
    ('employee','employee')
]

COURSE_STATUS = [
    ('enrolled','enrolled'),
    ('completed','completed'),
    ('ongoing','ongoing')

]


class Course(models.Model):
    course_name = models.CharField(null=True, blank=True, max_length=100)
    syllabus = models.CharField(null=True, blank=True, max_length=100)
    course_status = models.CharField(
        blank=True, null=True, choices=COURSE_STATUS, max_length=20
    )

    about_course = models.CharField(
        blank=True, null=True,  max_length=2000
    )
    batch_start_date = models.DateField(null=True)
    batch_end_date = models.DateField(null=True)


class Student(AbstractUser):
    username=None
    full_name = models.CharField(null=True,blank=True,max_length=200)
    mobile = models.CharField(blank=True,null=True,validators=[validate_mobile_number],max_length=20)
    password=models.CharField(null=True,blank=True,max_length=20)
    email = models.EmailField(null=True,blank=True)
    user_type = models.CharField(null=True,blank=True,choices=USER_CHOICES,max_length=10)
    enrolled_course = models.ForeignKey(Course,on_delete=models.DO_NOTHING,default="")

    def __str__(self):
        return self.username

    USERNAME_FIELD = "id"
    objects=UserManager()
    REQUIRED_FIELDS = []


# Create your models here.
