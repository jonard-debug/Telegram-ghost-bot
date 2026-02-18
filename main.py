from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio

API_ID = 24395315
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'
PHONE = '+2348130641310'

# !!! PUT THE NEW CODE TELEGRAM JUST SENT YOU HERE !!!
NEW_CODE = '92536' 

async def main():
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.connect()
    try:
        # This tries to sign in directly with the new code
        await client.sign_in(PHONE, NEW_CODE)
        print("\n🏆 SUCCESS! YOUR STRING SESSION IS: 🏆\n")
        print(client.session.save())
    except Exception as e:
        # If it asks for the 'Hash', it will print it here
        print(f"❌ NEED HASH: {e}")
        # If it fails, it will send a fresh code so we can try again
        await client.send_code_request(PHONE)
        print("🏛️ CHECK TELEGRAM AGAIN—IF A NEW CODE CAME, PUT IT IN AND COMMIT!")

asyncio.run(main())
