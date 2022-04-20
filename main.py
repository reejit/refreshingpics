from pyrogram import Client
import requests
from wget import download
from pyrogram.errors import FloodWait
import os
import time
from os import remove
from keep_alive import keep_alive
import asyncio
from asyncio import sleep
#import random
#from dotenv import load_dotenv

#load_dotenv()


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
        #headers = {'User-Agent': f"{random.randint(100000, 99999999)}"}
        file = "h.jpg"
        #await asyncio.sleep(1.5)
        start = time.time()
        url = requests.get("https://source.unsplash.com/random").url
        try:
            media = await bot.send_photo(chat_id, photo=url)
            media = media.message_id
            end = time.time()
            try:
              await bot.edit_message_caption(chat_id, media, f"Sent in {end - start:.2f} seconds")
            except FloodWait as e:
              print(f"Edit floodwait for {e.x}")
              await asyncio.sleep(e.x)
        except Exception as e:
            print(e)
            try:
                x = e.x
                print("{} seconds".format(x))
                await sleep(x)
                media = await bot.send_photo(chat_id, photo=url)
                media = media.message_id
                end = time.time()
                try:
                  await bot.edit_message_caption(chat_id, media, f"Sent in {end - start:.2f} seconds")
                except FloodWait as e:
                 print(f"Edit floodwait for {x}")
                 await asyncio.sleep(x)
            except Exception as e:
                print(e)
                download(url, file)
                try:
                    media = await bot.send_photo(chat_id, photo=file)
                    media = media.message_id
                    end = time.time()
                    try:
                      await bot.edit_message_caption(chat_id, media, f"Sent in {end - start:.2f} seconds")
                    except FloodWait as e:
                      print(f"Edit floodwait for {e.x}")
                      await asyncio.sleep(e.x)
                except FloodWait as e:
                    x = e.x
                    print("{} seconds".format(x))
                    await sleep(x)
                remove(file)


if __name__ == "__main__":
    keep_alive()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
