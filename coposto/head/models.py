from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from coposto.common import *


class Profile(TimeStampedModel):
    user = models.OneToOneField(User)
    passport_number = models.CharField(max_length=20, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], null=True,
                                    blank=True, max_length=20)
                                    # validators should be a list
    is_passport_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    success_rate = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.first_name + ', ' + self.email
