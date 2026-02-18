import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = '24395315'
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'

# 1. PUT YOUR PHONE NUMBER HERE (e.g., '+2348012345678')
PHONE = '+2348130641310' 

# 2. RUN THIS ONCE, IT WILL CRASH, BUT CHECK YOUR TELEGRAM FOR THE CODE
# 3. THEN PUT THE CODE TELEGRAM SENT YOU HERE
CODE = 'NONE' 

async def generate():
    async with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        if CODE == 'NONE':
            await client.send_code_request(PHONE)
            print("🏛️ CHECK YOUR TELEGRAM APP FOR THE LOGIN CODE!")
        else:
            await client.sign_in(PHONE, CODE)
            print("🏆 YOUR SESSION STRING IS BELOW: 🏆")
            print(client.session.save())
            print("🏆 COPY THE LONG TEXT ABOVE! 🏆")

asyncio.run(generate())
