import os
import sys
import json
import groupy

from groupy.client import Client

token = "Insert Access Token Here"

client = Client.from_token(token)

for group in client.groups.list_all():
   print(group.name)
