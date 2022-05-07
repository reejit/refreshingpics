#reejit/refreshingpics
from pyrogram import Client
from requests import get
import os
from os import remove
from asyncio import sleep, new_event_loop
from random import choice

# Imported all fu**ing libraries

#main function 👇

async def run():
#creating telegram object
    bot = Client(
        name=("ʀᴇꜰʀᴇꜱʜɪɴɢᴘɪᴄꜱ"),
        api_id=int(os.environ.get("API_ID")),
        api_hash=os.environ.get("HASH"),
        bot_token=os.environ.get("TOKEN"),
        no_updates=True,
        app_version="refershing1.3.1"
    )

 #getting chat_id passed as str like for @refreshingpics it's refreshingpics
    chat_id = os.environ.get("CHAT_ID")

 #starting bot otherwise throws error
    await bot.start()

#infine loop 🔁
    while True:
        list = ["https://source.unsplash.com/random","https://source.unsplash.com/random","https://source.unsplash.com/random", "https://picsum.photos/1080/1920","https://loremflickr.com/1080/1920"]
#chooshing random url because sometimes two bots tend to send same photos (at the same time).
        no = choice(list)
        url = get(no).url        
        try:
            await bot.send_photo(chat_id, photo=url)
        except Exception as e:
#maybe floodwait 420 or Telegram CURL failed 400
            print(e)
            try:
                x = e.value
                print("{} seconds".format(x))
#handled 420 error
                await sleep(x)
                await bot.send_photo(chat_id, photo=url)
#incase 400
            except Exception as e:
                print(e)
                from wget import download
                try:
                  file = download(url)
                except Exception:
                     print(Exception)
                     run()
                from pyrogram.errors import FloodWait
                try:
#incase 420 still exists
                    await bot.send_photo(chat_id, photo=file)           
                except FloodWait as e:
                    x = e.value
                    print("{} seconds".format(x))
                    await sleep(x)
#keeping memory free 😋
                remove(file)


if __name__ == "__main__":
    #keep_alive()
#running asynchronous
    loop = new_event_loop()
    loop.run_until_complete(run())
