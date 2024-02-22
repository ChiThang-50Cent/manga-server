from django.db import models
from user.models import CustomUser

# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE
    )
    
    description = models.TextField(default='')
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Chapter(models.Model):
    name = models.CharField(max_length=255)
    order = models.CharField(max_length=4, default=0)
    num_of_page = models.PositiveIntegerField()
    manga = models.ForeignKey(
        Manga,
        on_delete = models.CASCADE
    )
    post_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name