from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio

# CLEAN CREDENTIALS - NO QUOTES FOR ID
API_ID = 24395315
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'
PHONE = '2348130641310'

async def main():
    # We use a unique session name to force a fresh connection
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.connect()
    
    print("🏛️ ENGINE STARTING... TRIGGERING TELEGRAM NOW!")
    
    try:
        # This is the line that makes Telegram send the code immediately!
        sent_code = await client.send_code_request(PHONE)
        
        print(f"\n✅ SUCCESS! TELEGRAM SHOULD BE VIBRATING NOW!")
        print(f"🏆 NEW SECRET_HASH: {sent_code.phone_code_hash}")
        print("🏆 GET THE CODE FROM TELEGRAM AND TELL ME! 🏆")
        
    except Exception as e:
        print(f"❌ TELEGRAM IS BLOCKED: {e}")

asyncio.run(main())
