from telethon import events
from telethon import TelegramClient, sync
from Shyna_speech import Shyna_convodb
from Shyna_speech import Credentials_Shyna

api_id = Credentials_Shyna.tele_api_id()
api_hash = Credentials_Shyna.tele_api_hash()

client = TelegramClient('session_name', api_id, api_hash).start()

# Getting information about yourself
# me = client.get_me()
# print(me.stringify())


@client.on(events.NewMessage)
async def my_event_handler(event):
    if str(event.raw_text).lower().__contains__('shyna'):
        response = Shyna_convodb.shyna_for_tele('shyna')
        print(response, type(response))
        await event.reply(response)
    else:
        response=str(Shyna_convodb.shyna_for_tele(str(event.raw_text).lower()))
        await event.reply(response)

client.start()
client.run_until_disconnected()