from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print ("")
print ("")
print("""processing.......""")

API_KEY = '(2327886)'
API_HASH = "(b27fc6b63c22a6917438a57bc616075c)"
while True:
  try:
   with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
      print("")
      session = client.session.save()
      client.send_message("me", f"Here is your TELEGRAM STRING SESSION\n(tap to copy)👇 \n\n {session}")
      print("You telegram String session successfully stored in your telegram, please check your Telegram Saved Messages ")
      print(" Don't share it with anyone.. Regards.. KTech")
  except:
   print ("")
   print ("Wrong phone number \n make sure its with correct  country code")
   print ("")
   continue
  break
