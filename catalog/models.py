from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Syllabus(models.Model):
    title = models.CharField(max_length=255)
    description= models.TextField()
    upload_datetime=models.DateTimeField(auto_now_add=True)

# Django doesn't allows dynamic field creation within model class
class MCQmodel(models.Model):
    question=models.TextField(null=True)
    option1=models.CharField(max_length=255,null=True)
    option2=models.CharField(max_length=255,null=True)
    option3=models.CharField(max_length=255,null=True)
    option4=models.CharField(max_length=255,null=True)
    correct_option=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.question
    

# model for uploading previous year questions
class Previousyearqstnmodel(models.Model):
    rank_choices=[
        ('Officer','Officer level'),
        ('Section_officer','Section officer')
    ]
    rank = models.CharField(max_length=255,choices=rank_choices,null=True)
    title = models.CharField(max_length=255,null=True)#can use date in title,and later create individual hyperlink
    pdf = models.FileField(upload_to='past_questions/')
    upload_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# Model for uploading constitution

class Constitutionmodel(models.Model):
    title = models.CharField(max_length=255,null = True)
    pdf =  models.FileField(upload_to="Nepal_constitution/")

    def __str__(self):
        return self.title
    
# models for uploading the books pdf
class Bookmodel(models.Model):
    title = models.CharField(max_length=255,null=True)
    pdf = models.FileField(upload_to="Books/")

    def __str__(self):
        return self.title