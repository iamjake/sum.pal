import os
import sys
import json
import groupy

from groupy.client import Client
token = ""
client = Client.from_token(token)



def botTalkToGroup(botID,message,attach):
    client.bots.post(botID,message,attach)



def main():
    print("     == sum.Pal Bot ==       \n\n")

    groups = list(client.groups.list_all())
    for group in groups:
        print(group.name)

    # BOT TALKING TO GROUP #
    botTalkToGroup("22482b2e8f82a16f13242f93d8","david aint comin",[])




if __name__ == "__main__":
    main()