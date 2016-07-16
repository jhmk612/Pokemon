from django.db import models

# Create your models here.

class Post(models.Model):
    trainer_name=models.CharField(max_length=30)
    pokemon_name=models.CharField(max_length=50)
    lnglat=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def lng(self):
        return self.lnglat.split(',')[0]

    def lat(self):
        return self.lnglat.split(',')[1]

