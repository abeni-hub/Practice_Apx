from django.db import models

# Create your models here.
# models.py
from django.db import models

class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100)

class Course(models.Model):
    featured_img = models.ImageField(upload_to='course_img/', null=True, blank=True)
    course_name = models.CharField(max_length=100)
    title = models.TextField()
    features = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
class Scholarship(models.Model):
    name = models.CharField( max_length = 100)
    deadline = models.DateField(auto_now_add = True)   
    sponsorType =models.TextField()
    amount = models.DecimalField( max_digits = 10 , decimal_places = 2)
    UniversityName = models.CharField( max_length = 100)
    level = models.CharField(max_length = 100)
    study_field = models.CharField(max_length = 100)
    program = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to='scholarship_logo/')
    link = models.URLField()
    
    def __str__(self):
        return self.name
     

   