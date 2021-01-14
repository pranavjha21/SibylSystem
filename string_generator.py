from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details"""
)
APP_ID = int(input("2353687"))
API_HASH = input("375fb45eb1ba90f2b1cbf08a5cc06e02")
with TelegramClient(StringSession(1AZWarzYBu1z_1cYmyBBCY0n4gVTdVLEpTY_1gnGOwh6Vk8T40iCYaQz6Bfrq6b9oCGYt2ZWGiONuhwyWRkxNE1AcT7SAlol7U-yR7dpXEMIJB-cFz-cGyijYP4a3Eg-PXH_PMQpDa4MRLdHiv2XPsjz6_kaGybJmhio92y9b731UYB6Hh1Yc5NNhyLbXgymtA-lh5PK1QJo9SQgS3xgiSMdq1Th1RMltPYJn_XtmuinxdP13RjVQRkdK4yh-n1TMEImYkq5njB3EZOV6tvwQPmU6reg7yfASg3EZlQpFV_QFyULhiBm7CQIDD9Nma-lZ8aoF94qbKGWIaDoCnPN31sXtaH8d2Ks=), APP_ID, API_HASH) as client:
    print(client.session.save())
