# gradiantcolor->  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.227364, y2:0.858, stop:0 rgba(0, 0, 0, 255), stop:0.988636 rgba(68, 90, 25, 203));
# gradiantcolor->  background-color: qlineargradient(spread:pad, x1:1, y1:0.961, x2:0.03, y2:0.0463182, stop:0.037594 rgba(189, 0, 160, 179), stop:0.947368 rgba(0, 0, 0, 217));
# gradiantcolor->  background-color:qlineargradient(spread:pad, x1:0.977273, y1:0.945, x2:0.00568182, y2:0.024, stop:0 rgba(189, 0, 160, 174), stop:1 rgba(41, 41, 41, 198));
# import requests
"""
background-color:transparent;
border:2px solid qlineargradient(spread:pad, x1:0.716, y1:0, x2:0.517, y2:0.613409, stop:0.289773 rgba(151, 133, 210, 223), stop:0.926136 rgba(0, 183, 232, 239));
border-radius:6px;
"""







# api_id = 25024030
# api_hash = 'd61f15e860f17aae83252cb108abded6'
# import asyncio
# from pyrogram import Client
# from pyrogram.errors import UserPrivacyRestricted , ChatAdminRequired , PeerFlood
# def main():
#     with Client("profit", api_id, api_hash ) as app:
#         me = app.get_me()
#         print(me.phone_number)
#         hanlist = ["@turki7700","@asiri1439","@KSA1oo","@Elsaleemi"]
#         print("succecss log")
#         for handle in hanlist:
#             try:
#                 app.add_chat_members(chat_id = "@profitway05",user_ids=handle)
#                 print(f"succecss adding {handle}")
#             except UserPrivacyRestricted :
#                 print(f"{handle} The user privacy settings is Disabled auto invite")
#             except ChatAdminRequired :
#                 print("The method requires chat admin (you must be a Creator of channel)")
#                 break
#             except PeerFlood:
#                 print("can't be used because your account is banned currently limited")
#                 break
#             except Exception as e :
#                 print(e) 
# main()
# asyncio.run(main())


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