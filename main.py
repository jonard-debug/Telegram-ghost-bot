from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio

# NO QUOTES FOR ID, QUOTES FOR HASH AND PHONE
API_ID = 24395315
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'
PHONE = '2348130641310'

async def main():
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.connect()
    
    print("🏛️ REQUESTING FRESH CODE FOR SENIOR MAN...")
    try:
        sent_code = await client.send_code_request(PHONE)
        print(f"\n✅ SUCCESS! THE DOOR IS OPEN.")
        print(f"🏆 NEW SECRET_HASH: {sent_code.phone_code_hash}")
        print("🏆 CHECK YOUR TELEGRAM APP NOW! 🏆")
    except Exception as e:
        print(f"❌ ERROR: {e}")

asyncio.run(main())
