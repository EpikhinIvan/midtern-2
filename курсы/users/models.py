from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавьте сюда свои поля профиля, например:
    # bio = models.CharField(max_length=500)
    # location = models.CharField(max_length=30)
