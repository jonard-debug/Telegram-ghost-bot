from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio

# YOUR CREDENTIALS
API_ID = 24395315
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'
PHONE = '+2348130641310' # Put your number here!

# !!! PUT THE 5-DIGIT CODE FROM TELEGRAM HERE !!!
MY_CODE = '37969' 

async def main():
    try:
        # We use StringSession() to create the "Digital Passport"
        client = TelegramClient(StringSession(), API_ID, API_HASH)
        await client.connect()
        
        # This finishes the login using the code you just got
        await client.sign_in(PHONE, MY_CODE)
        
        print("\n🏆 SUCCESS! YOUR STRING SESSION IS BELOW: 🏆\n")
        print(client.session.save())
        print("\n🏆 COPY THE LONG TEXT ABOVE AND SAVE IT! 🏆")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    asyncio.run(main())
