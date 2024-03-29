
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    institute = models.CharField(max_length=100)
    stream = models.CharField(max_length=50)
    date   = models.DateField(auto_now_add=True,auto_now=False,null=True)

    def __str__(self):
        return f'{self.user.username} Profile {self.date}'

    ''' def save(self, *args, **kwargs):
        super().save( *args, **kwargs)

        img=Image.open(self.image.path)

        if img.height > 300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)'''