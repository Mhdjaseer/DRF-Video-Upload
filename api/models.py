from django.db import models

# Create your models here.

class Vedios(models.Model):
    title=models.CharField(max_length=100)
    vedio=models.FileField(upload_to='vedios/')
    time=models.DateTimeField()

    def __str__(self):
        return self.title