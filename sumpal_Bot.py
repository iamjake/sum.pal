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

# Access Token to use bot #
token = "dnQ98hYoQQjFlo5sYAN4mqoCTYLH0V0Ye8cOGvM9"


# bot : Not Evil Bot #
bot_ID = "22482b2e8f82a16f13242f93d8"
bot_name = "Not Evil Bot"

# This is for the group chat : bots Taking Over The World #
group_ID = 40061967

# Defines Full Access #
client = Client.from_token(token)


for group in client.groups.list_all():
   print(group.name)
userID = groupy.api.attachments.Mentions('mentions', '666')

messageLimit = 10

messageList = [ ]

groupMessages = groupy.api.messages.Messages(client.session,group_ID)

# FUNC: botTalkToGroup
# DETAILS: ID to the specific chat
#          MESSAGE to the item bot wants to convey
#          ATTACH to the images you would like to display alongside message
# NOTES: This will be removed later on
def botTalksWhenCalled(bot_ID, message,attach):
    client.bots.post(bot_ID, message, attach)

# FUNC: specificBotCall()
# DETAILS: This function will execute if called by user
# NOTES: To display correction, we use strHldr
def specificBotCall():
    call_Counter = 0
    if call_Counter == messageLimit:
        strHldr = ""
        for messageText in groupMessages.list(limit=call_Counter):
            strHldr = messageText.text + " " + strHldr + " "
            print(strHldr)

def main():
    groupMessages = groupy.api.messages.Messages(client.session,group_ID)
    print("\t\t**Sum.Pal Bot Starting**\n\n")
    
    recentMessageID = 0
    for messageText in groupMessages.list():
        recentMessageID = messageText.id
        break
    
    i = 0
    cmdIter = 0
    while(1):
        for messageText in groupMessages.list_since(recentMessageID):
            if messageText.name == bot_name:
                break
            strHolder = ""
            # BOT CMD SUMMARY #
            if "@sum.pal" in messageText.text:
                print(" ======== @@@@@ ========")
                for messageText in groupMessages.list_since(recentMessageID,limit = 1):
                    for messageText in groupMessages.list(limit=messageLimit):
                        if cmdIter == messageLimit:
                            break
                        strHolder = messageText.text + " " + strHolder + " "
                cmdIter += 1
                print(strHolder)
                summaryText = summaryMake(strHolder)
                if summaryText == -1:
                    summaryText = "No summary so far..."
                summaryText = summaryText.replace("@sum.pal","")
                botTalksWhenCalled(bot_ID, summaryText, [])
                cmdIter = 0
           #       specificBotCall()
           # botTalksWhenCalled(bot_ID, "I heard you!", [])
           # for messageText in groupMessages.list_all_after(recentMessageID,limit = 1):
           #    if "@sum.pal" in messageText.text:
           #        specificBotCall()
           #        botTalksWhenCalled(bot_ID, "I heard you!", [])
           #            recentMessageID = messageText.id

            # MESSAGE LIMIT SUMMARY #
                i = 0
            if i == messageLimit:
                print(" =========== limit ========")
                for messageText in groupMessages.list(limit=i):
                    strHolder = messageText.text + " " + strHolder + " "
                summaryText = summaryMake(strHolder)
                if summaryText == -1:
                    summaryText = "No summary so far..."
                summaryText = summaryText.replace("@sum.pal","")
                summaryText = summaryText.replace("\n","")
                botTalksWhenCalled(bot_ID, summaryText, [])
                print(summaryText)
                i = 0
            print(i)
            i += 1
            recentMessageID = messageText.id

if __name__ == "__main__":
    main()
