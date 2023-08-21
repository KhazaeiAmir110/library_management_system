from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone_number = models.CharField(_("phone_number"), max_length=11, unique=True, null=True)
    name = models.CharField(_("name"), max_length=50)
    age = models.IntegerField(null=True)
    image = models.ImageField(null=True, blank=True, upload_to='user_images')
    password = models.CharField(_("password"), max_length=128, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    STATUS_CHOICES = (
        ('S', _('Special')),
        ('N', _('Normal')),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    membership_validity_date = models.DateTimeField()

    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return str(self.phone_number)
