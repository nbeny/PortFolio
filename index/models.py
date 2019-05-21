from djongo import models
from django.urls import reverse


length = 255

class Contact(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    Name = models.CharField(max_length=length, help_text='Enter full name documentation')
    Email = models.CharField(max_length=length, help_text='Enter email documentation')
    Message = models.TextField(help_text='Enter message')

    #Metadata
    class Meta:
        ordering = ['Name', 'Email', 'Message']

    #Methods
    def get_absolute_url(self, *args, ** kwargs):
        return reverse('url', args=[args])
 
    def __str__(self):
        return self.Name


# from django.db import models

# # Create your models here.
# class profile(models.Model):
#     name = models.CharField(max_length=120)
#     description = models.TextField(default='description default text')
# #    location = models.CharField(max_length=120, default='my location default', blank=True, null=True)
# #    job = models.CharField(max_length=120, null=True)

#     def __str__(self):
#         return self.name