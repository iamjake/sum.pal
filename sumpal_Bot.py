import os
import sys
import json
import groupy


from groupy.client import Client
from groupy.api import messages
token = ""
botID = ""
groupID = ""
client = Client.from_token(token)



def botTalkToGroup(botID,message,attach):
    client.bots.post(botID,message,attach)



def main():
    print("     == sum.Pal Bot ==       \n\n")


    # BOT TALKING TO GROUP #
    #botTalkToGroup("22482b2e8f82a16f13242f93d8","david aint comin",[])

    # Bot listening ---------------------------------#

    # Get messages for SPECIFIC group #
    groupMessages = groupy.api.messages.Messages(client.session,groupID)
    #userID = groupy.api.attachments.Mentions("mentions", "44469965")
    # Get MOST RECENT message ID #
    recentMessageID = 0
    for messageText in groupMessages.list():
        recentMessageID = messageText.id
        break


    # Bot is now LISTENING #
    while(1):
        for messageText in groupMessages.list_since(recentMessageID):
            if "@bot" in messageText.text:
                print(" - @bot received")
                botTalkToGroup(botID,"@Anthony",[])
            recentMessageID = messageText.id


if __name__ == "__main__":
    main()