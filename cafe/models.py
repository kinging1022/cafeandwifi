from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class CafeList(models.Model):

    def __str__(self):
        return self.cafe_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    cafe_name = models.CharField(max_length=200)
    cafe_wifi = models.BooleanField(default=False)
    cafe_address = models.CharField(max_length=1000, default='N/A')
    cafe_rating = models.CharField(max_length=5, default='NIL')


    def get_absolute_url(self):
        return reverse("cafe:index")
