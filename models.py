from django.db import models

class Photo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/')
    
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
