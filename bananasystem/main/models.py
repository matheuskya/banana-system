from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank = True)
    profile_picture = models.ImageField(upload_to = 'profile_pics/', blank = True, null = True)
    location = models.CharField(max_length=50, blank = True)

    def __str__(self):
        return f'{self.user.username} Profile'
