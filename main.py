from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio

API_ID = '24395315'
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'
PHONE = '+234813064310'

async def main():
    # We use a fresh name 'final_attempt' to force a new request
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.connect()
    
    print("🏛️ REQUESTING FRESH CODE...")
    sent_code = await client.send_code_request(PHONE)
    
    print(f"\n✅ NEW CODE SENT TO TELEGRAM APP!")
    print(f"🏆 NEW SECRET_HASH: {sent_code.phone_code_hash}")
    print("🏆 LOOK AT YOUR TELEGRAM APP NOW! 🏆")

asyncio.run(main())
