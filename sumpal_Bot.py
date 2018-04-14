import os
import sys
import json
import groupy

from groupy.client import Client

# Access Token to use bot #
token = ""

# bot : Not Evil Bot #
bot_ID = ""

# This is for the group chat : bots Taking Over The World #
group_ID = 

client = Client.from_token(token)

#for group in client.groups.list_all():
#   print(group.name)

test_Chat = client.groups.get(group_ID)
#evil_Bot = client.bots.get(bot_ID)

#message = test_Chat.post(text)
