from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=50)
    singer = models.ForeignKey("api.Singer", on_delete=models.CASCADE, related_name='sungby')
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title