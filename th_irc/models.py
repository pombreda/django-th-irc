# -*- coding: utf-8 -*-

from django.db import models
from django_th.models.services import Services


class Irc(Services):

    # put whatever you need  here
    server = models.CharField(max_length=255)
    port = models.IntegerField()
    channel = models.CharField(max_length=20)
    channel_key = models.CharField(max_length=20, blank=True)
    nickname = models.CharField(max_length=20)

    # but keep at least this one
    trigger = models.ForeignKey('TriggerService')

    class Meta:
        app_label = 'django_th'
