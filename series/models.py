from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Series(models.Model):
    series_name=models.CharField(max_length=255, null=False, blank=True)
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    desc=models.TextField()
    Rank=models.IntegerField()
    year=models.DateTimeField(auto_now_add=True)
    Classification=models.CharField(max_length=255, null=False, blank=True)
    author=models.CharField(max_length=255, null=False, blank=True)
    actors=models.CharField(max_length=255, null=False, blank=True)


    def str(self):
        return self.series_name

