from django.db import models




class Functionality(models.Model):
    name= models.CharField(max_length=100, null=False, blank=False)
    description= models.TextField(max_length=100, null=False, blank=False)
        
    def __str__(self):
        return f"{self.name} - {self.description}"
    
    class Meta:
        verbose_name_plural = 'functionalities'
    
# Create your models here.
