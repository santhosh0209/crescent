from django.db import models

# Create your models here.


class blog(models.Model):
    image = models.ImageField(upload_to='images')
    date = models.DateField(auto_now=False)
    title = models.CharField(max_length=250)
    details = models.TextField(default=None)

    def __str__(self):
        return self.title
