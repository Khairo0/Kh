import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
print("</> Welcome to Tool 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ . </> ")
ch = "@SDBB_Bot"
api_id = '26031213'
api_hash = '15df916e4e17260afc4fa4ecde520968'
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open("Modca.txt").read().split("\n"):
    try:
        client.send_message(ch ,f"/chk {cc}")
        time.sleep(random.randint(42,60))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            t = str(mssag[0].message).split("again after ")[1]
            t = t.split("seconds")[0]
            t = int(t)
            print(f"Done Sleep : {t+2}")
            time.sleep(t+2)
        print(mssag[0].message)
        time.sleep(1)
    except:
        print(False)