from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from auth_app.models import CustomUser
from PIL import Image as Img
from django_image_app_api import settings
import os

SMALL_IMAGE_SIZE = (200, 200)
MEDIUM_IMAGE_SIZE = (400, 400)


class Image(models.Model):

    image = models.ImageField(upload_to=settings.IMAGE_STORE_PATH, null=True, default=None)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='image')
    link_lifetime_created = models.DateTimeField(null=True, blank=True)
    link_lifetime_in_seconds = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(300), MaxValueValidator(30000)])
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=False)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_variants()

    def delete(self, *args, **kwargs):
        path = self.image.path
        os.remove(path, dir_fd=None)
        os.remove(path.replace('.', '_medium.'), dir_fd=None)
        os.remove(path.replace('.', '_small.'), dir_fd=None)
        super(Image, self).delete(*args, **kwargs)

    def create_variants(self):
        path = self.image.path
        image = Img.open(path)

        small_image = image.copy()
        small_image.thumbnail(SMALL_IMAGE_SIZE)
        small_image.save(path.replace('.', '_small.'))

        medium_image = image.copy()
        medium_image.thumbnail(MEDIUM_IMAGE_SIZE)
        medium_image.save(path.replace('.', '_medium.'))
