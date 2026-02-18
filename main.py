import asyncio
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
import asyncio, random, requests
from telethon import TelegramClient, events, functions, types

# --- 🏛️ CEO BETHUEL'S CONTROL PANEL ---
# Paste your keys between the quotes below
API_ID = '2439531'
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'
COZE_TOKEN = 'pat_CAZ0y8INYfCERyDquWNbBO9yE1Scj313JRDVlMY4W1M166TclUk2XQDZMfC5xhkS'
BOT_ID = '8201261247:AAHLYVSH3ZhzYm0xuF-ZInILvpY0WRPbcyo'
# Your account details below
ACCOUNT_DETAILS = "BANK: OPAY | NAME: Bethuel Uchomada Odakwaji | ACCT: 7080421602"

client = TelegramClient('ghost_session', API_ID, API_HASH)

# Track sessions for the "Network Glitch" trick
user_sessions = {}

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    if not event.is_private: return
    
    sender_id = event.sender_id
    msg_text = event.message.message.lower()

    # --- 1. THE "NETWORK GLITCH" (Offline Trick) ---
    if sender_id not in user_sessions:
        user_sessions[sender_id] = asyncio.get_event_loop().time()
    
    elapsed = asyncio.get_event_loop().time() - user_sessions[sender_id]
    # After 5 minutes, go offline for 7 seconds to show "Last Seen Recently"
    if 300 <= elapsed <= 315: 
        print("💡 Senior Man Trick: Going Offline for 7s...")
        await client(functions.account.UpdateStatus(offline=True))
        await asyncio.sleep(7)
        await client(functions.account.UpdateStatus(offline=False))

    # --- 2. THE ACCOUNT DETAILS & GRACE TRICK ---
    payment_keywords = ['account', 'payment', 'pay', 'send money', 'acct', 'details', 'money']
    if any(word in msg_text for word in payment_keywords):
        # Trigger "Typing" for the grace message
        async with client.action(event.chat_id, 'typing'):
            await asyncio.sleep(4) 
            await event.respond("Look, I'm really not doing this because of the money. I have my own. I'm just doing this to help you move to the next level. 🤝⚖️")
        
        print("⏳ Waiting for user to read (Double Tick)...")
        while True:
            msg = await client.get_messages(event.chat_id, ids=event.id)
            if event.message.id <= (await client.get_input_entity(event.chat_id)).msg_id:
                 break
            await asyncio.sleep(2)

        # 7 seconds delay AFTER they read before sending account details
        async with client.action(event.chat_id, 'typing'):
            await asyncio.sleep(7) 
            await event.respond(f"Anyway, here are the details as you requested: \n\n{ACCOUNT_DETAILS}")
        return

    # --- 3. NORMAL AI CHAT (6-8s Typing) ---
    async with client.action(event.chat_id, 'typing'):
        delay = random.randint(6, 8) # Your custom speed
        print(f"Ghost is typing for {delay}s...")
        await asyncio.sleep(delay)
        
        url = "https://api.coze.com/v1/open_api/v1/chat"
        headers = {"Authorization": f"Bearer {COZE_TOKEN}", "Content-Type": "application/json"}
        data = {"bot_id": BOT_ID, "user_id": str(sender_id), "query": event.message.message, "stream": False}
        
        try:
            r = requests.post(url, headers=headers, json=data)
            if r.status_code == 200:
                messages = r.json().get('messages', [])
                for m in messages:
                    if m.get('type') == 'answer':
                        await event.reply(m.get('content'))
        except Exception as e:
            print(f"Error: {e}")

print("🏛️ CEO BETHUEL GHOST IS READY TO LAUNCH! 🚀")
client.start()
client.run_until_disconnected()
