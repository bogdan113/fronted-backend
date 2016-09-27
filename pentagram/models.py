from uuid import uuid1
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.


def photos_directory(instance, filename):
    return "photos/{user_id}/{uuid}-{filename}"\
        .format(user_id=instance.user.id,
                uuid=str(uuid1()),
                filename=filename)

def count(photo_id):
    return PhotoLike.objects.filter(photo=photo_id).count()

class Photo(models.Model):
    user = models.ForeignKey(User)
    photo = models.ImageField(upload_to = photos_directory, null = True, blank = True)
    like = models.IntegerField(default = 0)

    def __str__ (self):
        return str(self.id)


class Comment(models.Model):
    user = models.ForeignKey(User)
    comment = models.TextField()
    photo = models.ForeignKey(Photo)

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.comment)

class PhotoLike(models.Model):
    class Meta:
        unique_together = ('photo','user')
    user = models.ForeignKey(User, blank= False)
    photo = models.ForeignKey(Photo, null= True)


    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.photo)