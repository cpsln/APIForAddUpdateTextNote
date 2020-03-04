from django.db import models

# Create your models here.
class UrbanstopNotetext(models.Model):
    
    UserName = models.CharField(max_length=40)
    TextNote = models.CharField(max_length=1000)
    CreationDate = models.DateTimeField(auto_created=True, auto_now_add=True)
    UpdateDate = models.DateTimeField(null=True, blank=True)
    LastUpdateDate = models.DateTimeField(null=True, blank=True)
