from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    thumb = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class File(models.Model):
    name= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.filepath)