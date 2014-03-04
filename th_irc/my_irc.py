# -*- coding: utf-8 -*-
import sys
# add the python API here if needed
import irc.client

# django classes
from django.utils.log import getLogger

import irc.logging

# django_th classes
from django_th.services.services import ServicesMgr
from th_irc.models import Irc

"""
    handle process with irc
"""

logger = getLogger('django_th.trigger_happy')


class ServiceIrc(ServicesMgr):

    def save_data(self, token, trigger_id, **data):
        """
            let's publish the data
        """

        if data and data['link'] is not None and len(data['link']) > 0:
            # get the data of this trigger
            trigger = Irc.objects.get(trigger_id=trigger_id)

            # open a connection
            # TODO :
            # add a wait before posting ;
            # join once
            # left once

            client = irc.client.IRC()
            try:
                c = client.server().connect(
                    trigger.server, trigger.port, trigger.nickname)

            except irc.client.ServerConnectionError:
                print(sys.exc_info()[1])
                raise SystemExit(1)

            if trigger.channel_key:
                c.join(trigger.channel, key=trigger.channel_key)
            else:
                c.join(trigger.channel)

            text = ''
            text = (data['title'] + ' - ' + data[
                    'link'] if 'title' in data else data['link'])

            c.privmsg(trigger.channel, text)
            c.quit("Using irc.client.py")

            sentance = str('irc post {} on server {}/{} done').format(
                text, trigger.server, trigger.channel)
            logger.debug(sentance)
        else:
            logger.critical("no data provided for trigger ID %s ", trigger_id)
