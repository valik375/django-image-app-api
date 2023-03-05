import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from auth_app.managers import CustomUserManager


class CustomUser(AbstractUser):

    def name_file(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return '/'.join(['user_image', filename])

    USER_PLAN_BASIC = 1
    USER_PLAN_PREMIUM = 2
    USER_PLAN_ENTERPRISE = 3

    USER_PLAN_CHOICES = (
        (USER_PLAN_BASIC, 'Basic'),
        (USER_PLAN_PREMIUM, 'Premium'),
        (USER_PLAN_ENTERPRISE, 'Enterprise'),
    )

    username = None
    user_plan = models.IntegerField(choices=USER_PLAN_CHOICES, null=True)
    email = models.EmailField("email address", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.email
