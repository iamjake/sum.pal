# PROJECT: sumpal_Bot
# CONTRIBUTORS: Anthony See
#               Jacob Jurilla
# CREATION DATE: 04/14/18
# DESCRIPTION: Intelligent summarizer for GroupMe

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

# KEY(S) #
<<<<<<< HEAD
token = ""
bot_ID = ""
group_ID = 
=======
token = "Insert Key Here"
bot_ID = "Insert Key Here"
group_ID = 666
>>>>>>> 53ccbc3787502272ccdec3542add8d3f56717536

# GLOBAL VARIABLE(S) #
bot_name = "Not Evil Bot"
client = Client.from_token(token)
userID = groupy.api.attachments.Mentions('mentions', '666')
messageLimit = 10
messageList = []
groupMessages = groupy.api.messages.Messages(client.session, group_ID)

# FUNC: botTalkToGroup
# DETAILS: ID to the specific chat
#          MESSAGE to the item bot wants to convey
#          ATTACH to the images you would like to display alongside message
# NOTES: This will be removed later on
def botTalksWhenCalled(bot_ID, message, attach):
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

# FUNC: reformatText()
# DETAILS: Formats the Text for every call
# NOTES: Will take in username, summary
def reformatText(username, summaryText, format):
    textHeader = ""

    summaryText = summaryText.replace("@sum.pal", "")
    summaryText = summaryText.replace("\n", "")

    if format == "cmd":
        textHeader = ("Here is a recap %s :\n" % (username))

    if format == "limit":
        textHeader = ("Here is what I got so far : \n")

    reformatString = textHeader + summaryText
    return reformatString


def buildSummary( strHolder, currentUser, mode ):
    summaryText = summaryMake(strHolder)
    if summaryText == -1:
        summaryText = "No summary so far..."
    finalText = reformatText(currentUser, summaryText, mode)
    botTalksWhenCalled(bot_ID, finalText, [])



def main():
    groupMessages = groupy.api.messages.Messages(client.session, group_ID)
    print("\t\t****Sum.Pal Bot Starting****\n\n")

    recentMessageID = 0
    for messageText in groupMessages.list():
        recentMessageID = messageText.id
        break

    i = 0
    cmdIter = 0
    
    while (1):
        for messageText in groupMessages.list_since(recentMessageID):
            if messageText.name == bot_name:
                break
            currentUser = messageText.name
            strHolder = ""

            # BOT CMD SUMMARY #
            if "@sum.pal" in messageText.text:
                print("======== @sum.pal CAUGHT ========")
                for messageText in groupMessages.list(limit=messageLimit):
                    if cmdIter == messageLimit:
                        break

                    # DON'T PICK UP BOT TEXT #
                    if messageText.name != bot_name:
                        strHolder = messageText.text + " " + strHolder + " "
                        cmdIter += 1

                # BUILD SUMMARY #
                buildSummary(strHolder, currentUser, "cmd")
                cmdIter = 0
                i = 0

            # MESSAGE LIMIT SUMMARY #
            if i == messageLimit:
                print("=========== Limit CAUGHT ========")
                for messageText in groupMessages.list(limit=i):
                    # Do not pick up bot text #
                    if messageText.name != bot_name:
                        strHolder = messageText.text + " " + strHolder + " "

                # Build Summary #
                print(strHolder)
                buildSummary(strHolder, currentUser, "limit")
                i = 0

            print(i)
            i += 1
            recentMessageID = messageText.id


if __name__ == "__main__":
    main()
