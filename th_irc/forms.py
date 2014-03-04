# -*- coding: utf-8 -*-

from django import forms
from th_irc.models import Irc


class IrcForm(forms.ModelForm):

    """
        for to handle Pocket service
    """

    class Meta:
        model = Irc
        fields = ('server', 'port', 'channel', 'channel_key', 'nickname')


class IrcProviderForm(IrcForm):
    pass


class IrcConsummerForm(IrcForm):
    pass
