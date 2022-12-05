# gradiantcolor->  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.227364, y2:0.858, stop:0 rgba(0, 0, 0, 255), stop:0.988636 rgba(68, 90, 25, 203));
# gradiantcolor->  background-color: qlineargradient(spread:pad, x1:1, y1:0.961, x2:0.03, y2:0.0463182, stop:0.037594 rgba(189, 0, 160, 179), stop:0.947368 rgba(0, 0, 0, 217));
# gradiantcolor->  background-color:qlineargradient(spread:pad, x1:0.977273, y1:0.945, x2:0.00568182, y2:0.024, stop:0 rgba(189, 0, 160, 174), stop:1 rgba(41, 41, 41, 198));
# import requests
"""
background-color:transparent;
border:2px solid qlineargradient(spread:pad, x1:0.716, y1:0, x2:0.517, y2:0.613409, stop:0.289773 rgba(151, 133, 210, 223), stop:0.926136 rgba(0, 183, 232, 239));
border-radius:6px;
"""

# from telethon import TelegramClient, events, sync
# from telethon.tl.functions.channels import JoinChannelRequest
from time import sleep
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.

api_id = 28013226

api_hash = 'e0330d20097370f2e70231c202a2df13'

from telethon.sync import TelegramClient
from telethon import functions
from telethon import types

client = TelegramClient("session", api_id, api_hash) 
client.start()

# # Invite to channel  ------------------
# result = client(functions.channels.InviteToChannelRequest(
#     channel = 'k7hhm' ,
#     users = ["@shw_503"] ,
# ))
# print(result.stringify())

# getIDs from group
# res = client(functions.channels.GetParticipantsRequest(
#     channel = "Shmnaif" ,
#     filter = types.ChannelParticipantsSearch("") ,
#     offset = 100 ,
#     limit = 100 ,
#     hash = -12398745604826 ,
# ))
# print(res.count)
# print(res.participants[2].user_id)


result = client(functions.channels.GetParticipantsRequest(
    channel= "Shmnaif" , 
    filter = types.ChannelParticipantsSearch("") ,
    offset = 2000 ,
    limit = 2000 ,
    hash = -12398745604826 ,

))

print(len(result.users))
print(result.users[0].username)





# from telethon.sync import TelegramClient


# session_path = "sessions.session"
# if not session_path.exists():
#     session_path.mkdir()

# # phone_number = get_phone_number()
# client = TelegramClient(f"sessions", api_id, api_hash)#, proxy=proxy


# async def main():
#     await client.connect()

#     await client.send_code_request(f"+201554071240", force_sms=True)
#     verification_code = client.get_verification_code()
#     await client.sign_up(verification_code, names.get_first_name(), names.get_last_name())

#     await client.disconnect()


# client.loop.run_until_complete(main())


class Styles():
    BUTTON = """
    QPushButton{
        color:white;/*
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(68, 90, 25, 203));
        */border-radius:4px;

    }
    QPushButton:hover{
        color:black;
        background-color:white;
    }"""
    PROGRESSBAR = """
    QProgressBar {

        background-color:transparent;
        color: white;
        border-style: outset;
        border-width: 2px;
        border-color: #74c8ff;
        border-radius: 7px;
        font: bold 10px;
        text-align:center; 
    }
    QProgressBar::chunk {
        border-radius: 6px;
        background-color:#686868;
    }"""