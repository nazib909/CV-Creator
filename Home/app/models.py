from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Edu(models.Model):
    DEGREE_CHOICES = (
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
        ('BSC', 'BSC')
    )
    degree = models.CharField(max_length=5, choices=DEGREE_CHOICES)
    institution = models.CharField(max_length=50, null=True, blank=True)
    gpa = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Skill(models.Model):
    s_name = models.CharField(max_length=30)
    proficiency = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Project(models.Model):
    p_name = models.CharField(max_length=30)
    des = models.TextField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Experience(models.Model):
    j_title = models.TextField(max_length=30)
    c_name = models.TextField(max_length=30)
    location = models.TextField(max_length=30, null=True, blank=True)
    des = models.TextField(max_length=255, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Language(models.Model):
    FLUENCY = (
        ('Native', 'Native'),
        ('Professional', 'Professional')
    )
    name = models.CharField(max_length=20)
    fluency = models.CharField(max_length=30, choices=FLUENCY)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Interest(models.Model):
    name = models.TextField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Contact(models.Model):
    email = models.EmailField(max_length=30)
    phone = models.TextField(max_length=11)
    portfoliosite = models.TextField(max_length=100, null=True, blank=True)
    linkedin = models.TextField(max_length=100, null=True, blank=True)
    github = models.TextField(max_length=100, null=True, blank=True)
    twitter = models.TextField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Profile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name = models.CharField(max_length=50)

    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    carrier_profile = models.TextField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
