"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: @mrconfused
Edited: Jarvis UserBot
"""
import asyncio
import io 
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in heroku vars"
PREV_REPLY_MESSAGE = {}

@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if not event.is_private:
            return
        PM = ("`Hello. You are accessing the availabe menu of my peru master,`"
              f"{DEFAULTUSER}.\n"
               "__Let's make this smooth and let me know why you are here ! So Select A Reason And Send it's Number__\n"
               "**Choose one of the following reasons why you are here:**\n\n"
               "`1`. To chat with my master\n"
               "`2`. To Spam my master's Inbox.\n"
               "`3`. To enquire something\n"
               "`4`. To request something\n")
        ONE = ("`I Have Registered Your Request ! Don't Worry My Master Will Be Here Soon To Chat With You !` \n\n")
        TWO = ("`Please Don't Spam My Master Inbox ! You Have Been Reported Until Further Notice !`")
        FOUR = ("`Okay ! I See You Can Request Your Demands ! Please Wait Untill My Master Approves You` !")
        FIVE = ("`Okay. please have the basic manners as to not bother my master too much. If he wishes to help you, he will respond to you soon.`\n**Kindly Do not ask repeatdly else you will be blocked and reported.**")
        LWARN = ("**This is your last warning. DO NOT send another message else you will be blocked and reported. Keep patience. My master will respond you ASAP.**\n__Use__ `/start` __to go back to the main menu.__")
     
        async with borg.conversation(chat) as conv:
         if pmpermit_sql.is_approved(chat_id):
            return
         await borg.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "1":
             if pmpermit_sql.is_approved(chat_id):
                return
             await borg.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "/start":
                 await response.delete()
                 if pmpermit_sql.is_approved(chat_id):
                    return
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     if pmpermit_sql.is_approved(chat_id):
                            return
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "2":
             if pmpermit_sql.is_approved(chat_id):
                    return
             await borg.send_message(chat, LWARN)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 if pmpermit_sql.is_approved(chat_id):
                        return
                 await borg.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "3":
             if pmpermit_sql.is_approved(chat_id):
                    return
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             if not response.text == "/start":
                 if pmpermit_sql.is_approved(chat_id):
                    return
                 await borg.send_message(chat, LWARN)
                 await event.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     if pmpermit_sql.is_approved(chat_id):
                            return
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "4":
             if pmpermit_sql.is_approved(chat_id):
                    return
             await borg.send_message(chat,FIVE)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 if pmpermit_sql.is_approved(chat_id):
                        return
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     if pmpermit_sql.is_approved(chat_id):
                            return
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             if pmpermit_sql.is_approved(chat_id):
                    return
             await borg.send_message(chat, "`You have entered an invalid command. Please send /start again or do not send another message if you do not wish to be blocked and reported.`")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "/start":
                 if pmpermit_sql.is_approved(chat_id):
                    return
                 await borg.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "/start":
                     if pmpermit_sql.is_approved(chat_id):
                        return
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
