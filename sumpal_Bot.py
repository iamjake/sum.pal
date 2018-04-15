import groupy
import json
import os
import random
import sys
import time

from groupy.client import Client
from groupy.api import messages
from groupy.api import attachments

time.ctime()

# Access Token to use bot #
token = ""

# bot : Not Evil Bot #
bot_ID = ""

# This is for the group chat : bots Taking Over The World #
group_ID = 

# Defines Full Access #
client = Client.from_token(token)

userID = groupy.api.attachments.Mentions('mentions', '666')

messageLimit = 3

messageList = [ ]

groupMessages = groupy.api.messages.Messages(client.session,group_ID)


def botInitialPost(bot_ID, message):
    client.bots.post(bot_ID, message)


# FUNC: botTalkToGroup
# DETAILS: ID to the specific chat
#          MESSAGE to the item bot wants to convey
#          ATTACH to the images you would like to display alongside message
# NOTES: This will be removed later on
def botTalksWhenCalled(bot_ID, message,attach):
    client.bots.post(bot_ID, message, attach)


# To get name,
# for messageText in groupMessages.list(limit=i):
#   moveToList(messageText.name)
def moveToList(messageText):
    #for messageText in groupMessages.list():
    messageList.append(messageText)
    print(messageList)





def main():
    groupMessages = groupy.api.messages.Messages(client.session,group_ID)
    print("\t\t**Sum.Pal Bot Starting**\n\n")
    botInitialPost(bot_ID,"The Evil Bot has started, current time")
    botInitialPost(bot_ID, str(time.ctime()))
    
    recentMessageID = 0
    for messageText in groupMessages.list():
        recentMessageID = messageText.id
        break
    
    i = 0
    while(1):
        for messageText in groupMessages.list_since(recentMessageID):
            if "@sum.pal " in messageText.text:
                print("Bot was mentioned.\n")
                botTalksWhenCalled(bot_ID, "I heard you!", [])
            recentMessageID = messageText.id
            i += 1
            if i == messageLimit:
                for messageText in groupMessages.list(limit=i):
                    moveToList(messageText.text)
                    print("Message from user contains {}".format(messageText.text))
                i = 0
            print(i)

if __name__ == "__main__":
    main()
