from ast import Mod
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from base.models import Application, Advice


# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    profile_pic = models.ImageField(default='default.png', upload_to='Profiles')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()
    #     img = Image.open(self.profile_pic.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_pic)
