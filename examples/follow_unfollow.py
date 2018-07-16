#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this is an example for how to follow and unfollow specific user accounts
# works best with several accounts

import sys, os
sys.path.append(os.path.join(sys.path[0],'src'))

from instabot import InstaBot
from check_status import check_status
from feed_scanner import feed_scanner
from unfollow_protocol import unfollow_protocol
from follow_protocol import follow_protocol
import time

# change this username & password
bot = InstaBot(login="username", password="password")
bot.unfollow('instagram id ex. 12281817')

#follow
bot.follow('instagram id')