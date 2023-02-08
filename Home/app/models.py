from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Edu(models.Model):
    degree = models.CharField(max_length=5)
    institution = models.CharField(max_length=50, null=True, blank=True)
    passingyear = models.CharField(max_length=4, null=True, blank=True)
    def __str__(self):
        return str(self.degree)


class Skill(models.Model):
    s_name = models.CharField(max_length=30)
    proficiency = models.PositiveIntegerField()
    def __str__(self):
        return str(self.s_name)


class Project(models.Model):
    p_name = models.CharField(max_length=30)
    des = models.TextField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.p_name)


class Experience(models.Model):
    j_title = models.TextField(max_length=30)
    c_name = models.TextField(max_length=30)
    duration = models.CharField(max_length=255,null=True,blank=True)
    des = models.TextField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.j_title)
    


class Language(models.Model):
    l_name = models.CharField(max_length=20)
    fluency = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return str(self.l_name)


class Interest(models.Model):
    i_name = models.TextField(max_length=30)
    def __str__(self):
        return str(self.i_name)


class Contact(models.Model):
    email = models.EmailField(max_length=30)
    phone = models.TextField(max_length=11)
    portfolio = models.TextField(max_length=100, null=True, blank=True)
    linkedin = models.TextField(max_length=100, null=True, blank=True)
    github = models.TextField(max_length=100, null=True, blank=True)
    twitter = models.TextField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.email)


class Profile(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    carrier_profile = models.TextField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    edus = models.ManyToManyField(Edu)
    skills = models.ManyToManyField(Skill)
    projects = models.ManyToManyField(Project)
    experiences = models.ManyToManyField(Experience)
    languages = models.ManyToManyField(Language)
    interests = models.ManyToManyField(Interest)
    contacts = models.OneToOneField(Contact,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
