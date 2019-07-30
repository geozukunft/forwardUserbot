import asyncio
import datetime
import os
import time

import schedule
import telethon
import telethon.sync






with telethon.sync.TelegramClient('geosession', api_id, api_hash, lang_code='de') as client:
    me = client.get_me()

    username = me.username
    print(username)
    print(me.phone)