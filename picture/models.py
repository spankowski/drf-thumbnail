from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class TempPictureModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='media/')

    published_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    expire_time = models.IntegerField(blank=True, null=True,  validators=[
            MaxValueValidator(30000),
            MinValueValidator(300)
        ])
    expired = models.DateTimeField(blank=True, null=True)
   
    def save(self, *args, **kwargs):
        if (self.expire_time is not None):
            try:
                self.expired = timezone.now() + timezone.timedelta(seconds=self.expire_time)
                super(TempPictureModel, self).save(*args, **kwargs) # Call the "real" save() method.
            except:
                print('Error')
        else:
            super(TempPictureModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
                             