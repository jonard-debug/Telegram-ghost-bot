from telethon.sync import TelegramClient
import asyncio

API_ID = 24395315
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'
PHONE = '++2348130641310' # Put your number here!

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(PHONE)
        print("🏛️ CODE SENT! CHECK YOUR TELEGRAM APP NOW!")

asyncio.run(main())
