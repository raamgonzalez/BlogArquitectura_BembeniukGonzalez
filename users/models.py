from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_image', default = 'default.png')
    descripcion	= models.CharField(max_length=255)
    link_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Pefil de usuario'
        verbose_name_plural = 'Perfiles de usuarios'
