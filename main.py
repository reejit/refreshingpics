from pyrogram import Client
import requests
import os
from os import remove
#from keep_alive import keep_alive
import asyncio
from asyncio import sleep
import random
list = ["https://source.unsplash.com/random","https://source.unsplash.com/random","https://source.unsplash.com/random", "https://picsum.photos/1080/1920",]
async def run():
    bot = Client(
        api_id=os.environ.get("API_ID"),
        api_hash=os.environ.get("HASH"),
        bot_token=os.environ.get("TOKEN"),
        session_name=":memory:",
    )
    chat_id = os.environ.get("CHAT_ID")
    await bot.start()
    while True:
        file = "h.jpg"
        random.shuffle(list)
        random.shuffle(list)
        no = random.choice(list)
        print(no)
        url = requests.get(no).url
        try:
            await bot.send_photo(chat_id, photo=url)
        except Exception as e:
            print(e)
            try:
                x = e.x
                print("{} seconds".format(x))
                await sleep(x)
                await bot.send_photo(chat_id, photo=url)
            except Exception as e:
                print(e)
                from wget import download
                download(url, file)
                from pyrogram.errors import FloodWait
                try:
                    await bot.send_photo(chat_id, photo=file)           
                except FloodWait as e:
                    x = e.x
                    print("{} seconds".format(x))
                    await sleep(x)
                remove(file)


if __name__ == "__main__":
    #keep_alive()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run())
