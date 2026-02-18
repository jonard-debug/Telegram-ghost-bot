from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio

API_ID = '24395315'
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'
PHONE = '+2348130641310'

async def main():
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.connect()
    # This sends the code and PRINTS the secret hash we need
    sent_code = await client.send_code_request(PHONE)
    print(f"\n🏛️ CODE SENT! CHECK TELEGRAM.")
    print(f"🏆 YOUR SECRET_HASH IS: {sent_code.phone_code_hash}\n")

asyncio.run(main())
