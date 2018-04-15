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
token = ""


# bot : Not Evil Bot #
bot_ID = ""

# This is for the group chat : bots Taking Over The World #
group_ID = 

# Defines Full Access #
client = Client.from_token(token)


for group in client.groups.list_all():
   print(group.name)
userID = groupy.api.attachments.Mentions('mentions', '666')

messageLimit = 10

messageList = [ ]

groupMessages = groupy.api.messages.Messages(client.session,group_ID)


#def botInitialPost(bot_ID, message):
#    client.bots.post(bot_ID, message)


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
    # botInitialPost(bot_ID,"The Evil Bot has started, current time")
    # botInitialPost(bot_ID, str(time.ctime()))
    
    recentMessageID = 0
    for messageText in groupMessages.list():
        recentMessageID = messageText.id
        break
    
    i = 0
    cmdIter = 0
    while(1):
        for messageText in groupMessages.list_since(recentMessageID):
            #print(" MESSAGE : %s" % (messageText.text))
            strHolder = ""

            # bot cmd summary #
            if "@sum.pal" in messageText.text:
                print(" ======== @@@@@ ========")
                for messageText in groupMessages.list_since(recentMessageID,limit = 1):
                    for messageText in groupMessages.list(limit=messageLimit):
                    if cmdIter == 3:
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
                i = 0
            #       specificBotCall()
            #botTalksWhenCalled(bot_ID, "I heard you!", [])
           
           #for messageText in groupMessages.list_all_after(recentMessageID,limit = 1):
           #    if "@sum.pal" in messageText.text:
           #        specificBotCall()
           #        botTalksWhenCalled(bot_ID, "I heard you!", [])
           #            recentMessageID = messageText.id

            # message limit summary #
            
            elif i == messageLimit:
                print(" =========== limit ========")
                for messageText in groupMessages.list(limit=i):
                    strHolder = messageText.text + " " + strHolder + " "
            #print(strHolder)

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

