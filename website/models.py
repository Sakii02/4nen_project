from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('レビュー', max_length=1000)

    def __str__(self):
        return self.title