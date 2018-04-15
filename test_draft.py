import groupy
import json
import os
import random
import sys
import time

from sumpal_Algo import *
from groupy.client import Client
from groupy.api import messages
from groupy.api import attachments

time.ctime()


token = "Insert Access Token Here"

# Access Token to use bot #
token = "dnQ98hYoQQjFlo5sYAN4mqoCTYLH0V0Ye8cOGvM9"


# bot : Not Evil Bot #
bot_ID = "22482b2e8f82a16f13242f93d8"

# This is for the group chat : bots Taking Over The World #
group_ID = "40061967"

# Defines Full Access #
client = Client.from_token(token)


for group in client.groups.list_all():
    print(group.name)

userID = groupy.api.attachments.Mentions('mentions', '666')

messageLimit = 5

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
    cmdIter = 0
    while(1):
        for messageText in groupMessages.list_since(recentMessageID):
            if "@sum.pal" in messageText.text:
                for messageText in groupMessages.list_all_before(recentMessageID,limit = 2):
                    if cmdIter == messageLimit:
                        break
                    print("cmdTest: ",messageText.text)
                    cmdIter += 1
                
                print("Bot was mentioned.\n")
                botTalksWhenCalled(bot_ID, "I heard you!", [])
            recentMessageID = messageText.id
            
            i += 1
            if i == messageLimit:
                strHolder = ""
                for messageText in groupMessages.list(limit=i):
                    strHolder = messageText.text + " " + strHolder + " "
                    print(strHolder)
                summaryText = summaryMake(strHolder)
                botTalksWhenCalled(bot_ID,summaryText,[])
                print(summaryText)
                i = 0
    print(i)

if __name__ == "__main__":
    main()

