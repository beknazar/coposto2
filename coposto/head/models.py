from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from coposto.common import TimeStampedModel


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


class Group(TimeStampedModel):
    done = models.BooleanField(default=False)


class Parcel(TimeStampedModel):
    profile_a = models.ForeignKey(Profile, related_name='profile_a_parcel')

    # destination_a = models.ForeignKey(City_Russian, related_name='destination_a_parcel')
    # destination_b = models.ForeignKey(City_Russian, related_name='destination_b_parcel')

    done = models.BooleanField(default=False)
    date_a = models.DateField()
    date_b = models.DateField()
    parcel_name = models.CharField(max_length=100)
    description = models.TextField(default='')
    price = models.FloatField()
    weight = models.FloatField()
    is_featured = models.BooleanField(default=False)
    group = models.ForeignKey(Group, blank=True, related_name='senders')
    win = models.PositiveIntegerField(default=0)
