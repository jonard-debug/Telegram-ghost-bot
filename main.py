from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import random

# --- [1. THE ENGINE CREDENTIALS] ---
API_ID = 24395315
API_HASH = '9ea9861f2c047bb3ebc0de86675c0238'
# Paste your long String Session code inside the quotes below! 🔑
STRING_SESSION = '1BJWap1wBu7xruqiHhw99ROPbxaHkn3_yQO4LzB307PdVCSfiooSiKmi__sZYlSSM7nanlumUgyDQx0nw6J37M9GwbmOt6RdWFi7NvwF0to8avJ7XsBggh44nKYsOUUKH-KXpFM6hCVLgylZimAJKp0LDWWA3LLn_h0qH8CXFh6-NCyluOp1Erm2Qrrf-OXJP0gUI2Y2q0U6ToCS3STHcqrY7Vo18cDyZ363TylG_G-Gn8JJixDpyaObQtWMTjV-hHeLqZ3l6mbNp4ghv7Ua15rqILc07cdlYA0EnbtjQDc50qJlFo5ci_8oPNaJavgfpRDTOPwcDtUrXPEX8HVTOPNj6DQwLnV0=' 

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

# --- [2. GHOST BRAIN STORAGE] ---
user_data = {}  
random_chat_count = {} 

# --- [3. THE SCRIPT ENGINE] ---
def get_funnel_text(step, u_type, name=None, dream=None):
    source_msg = {
        "gemini": "coming from the group for the 1.7M Gift",
        "facebook": "coming from my Facebook post regarding the 1.7M Gift",
        "instagram": "coming from my Instagram updates regarding the 1.7M Gift",
        "universal": "coming to claim your spot in the 1.7M Gift"
    }
    source = source_msg.get(u_type, source_msg["universal"])

    steps = {
        1: f"Welcome to the Velocity Lane, {name}. 🏎️💨\n\nI see you’re {source}. I’m currently attending to about 4 other people who jumped in first, but I want to be sure you're actually ready for this. 🧐🏛️\n\nJust to confirm: You saw the ₦1.7M Value breakdown and you’re ready to use the J-System to accelerate your income this month? I don't want to waste your time or mine if you aren't ready to move at Senior Man speed. 🥊🏁\n\nShould I proceed with your slot, or are you still just 'thinking' about it? 🧐🏎️💨",
        2: "Good. I like the energy. 🤝🔥\n\nThe update is the 'J-System Digital Acceleration.' Like I said, it’s the result of 3 months of hard testing and real-world alerts. 🏛️📈\n\nSee, I realized that having an AI tool like Gemini is good, but without a 'System,' it's just a dead Ferrari. The J-System is the engine, the key, and the fuel. It’s the framework that turns Gemini from a 'chatbot' into a Daily Alert Machine. 📲💰🏎️💨",
        3: "But before I open the vault, I want you to do something for me. 🤫 Just stop for a second and imagine something. 🧘‍♂️\n\nImagine it’s 14 days from now. You pick up your phone by 10 AM, and instead of 'Sapa' notifications, you see ₦50k, ₦100k, or even ₦200k in daily credit alerts because you finally aligned Gemini with a proven system. 🏦📈\n\nIf money stopped being a problem today because of this 1.7M Gift, what is the FIRST thing you would do? 🧐💎",
        4: f"That's a beautiful dream, {name}, and it’s 100% possible. 🤝✨ \n\nBut let me be very clear, this is NOT Affiliate Marketing, Crypto, or Ponzi schemes. ❌ This is a NEW system. When you get the J-System Blueprint, you claim a 'Wealth Vault' totaling ₦1,750,000:\n\n💎 MASTER BLUEPRINT (₦450k)\n🤖 AI GEMINI ENGINE (₦250k)\n🎨 PRO DESIGN TOOLS (₦150k)\n📝 DM SCRIPTS (₦200k)\n💡 NO-NEPA HACK (₦150k)\n🤝 VIP INNER CIRCLE (₦350k)\n\nTOTAL VALUE: ₦1,750,000 🏦💸🥊\n\nI’m selecting 10 action-takers. Should I send the access link to you first, or let the next person in line take your gift? 🧐⏳🔥",
        5: "I hear the hunger, and honestly, that’s why I’m doing this. 🤝✨\n\nI’m not charging you ₦1.75 Million. ❌ I’m not even charging you ₦100k. ❌\n\nIf you are among the first 10 people right now, you get the entire 1.7M Wealth Vault for just ₦10,000. 🏧🔥\n\nDo you want me to drop the account details now, or move to the next person? 🧐💳🔥",
        6: "I hear you, but the J-System moves at the speed of light. 🏎️💨 By the time you come back, the 10 slots will be gone. The ₦10k isn't the problem; the lack of a system is the problem. 🛡️📉\n\nBANK: [Opay]\nACCT NO: [7080421602]\nNAME: [Bethuel Uchomada Odakwaji]\n\nIf the 10k hits in 1 hour, the gift is yours. If not, I will have to Refund you immediately. Are you 'Next Week' or 'Next Level'? ⏳🔥"
    }
    return steps.get(step, "")

async def typing_delay(chat_id):
    async with client.action(chat_id, 'typing'):
        # FIXED 10-15s DELAY AS REQUESTED ⏳
        await asyncio.sleep(random.randint(10, 15)) 

@client.on(events.NewMessage(incoming=True))
async def ghost_logic(event):
    if not event.is_private: return
    user_id = event.sender_id
    msg = event.text.lower()
    
    # --- FAREWELL LOGIC (STOP REPLIES AFTER GOODBYE) ---
    if any(word in msg for word in ["bye", "goodnight", "stop", "later"]):
        await typing_delay(event.chat_id)
        await event.reply("No problem, Senior Man! 🏛️ We'll talk later. Stay sharp! 🏎️💨")
        # Mark as finished so it won't reply again
        user_data[user_id] = {'step': 'finished'} 
        return

    if user_id in user_data and user_data[user_id].get('step') == 'finished':
        return # STOP MESSAGING 🛑

    if user_id not in user_data:
        if "gemini" in msg or "1.7m" in msg: u_type = "gemini"
        elif "facebook" in msg or "fb" in msg: u_type = "facebook"
        elif "instagram" in msg or "ig" in msg: u_type = "instagram"
        else: u_type = "universal"
        user_data[user_id] = {'step': 'get_name', 'name': 'Boss', 'dream': '', 'type': u_type}
        random_chat_count[user_id] = 0
    u = user_data[user_id]

    # --- ANTI-SCAM BRIDGE 😂 ---
    if any(word in msg for word in ["scam", "fraud", "legit", "fake", "real"]):
        await typing_delay(event.chat_id)
        await event.reply("Hahaha! 😂 Honestly, I love that you asked that. If I was a scammer, would I be taking the time to explain a full system to you? 🧐 I’m here to help you accelerate, not play games. 😊\n\nShould we continue with your slot? 🏎️💨")
        return

    # --- STEP-BY-STEP FUNNEL ---
    if u['step'] == 'get_name':
        if "name is" in msg or len(msg.split()) < 3:
            u['name'] = event.text.split("is")[-1].strip() if "is" in msg else event.text
            u['step'] = 1
            await typing_delay(event.chat_id)
            await event.reply(get_funnel_text(1, u['type'], name=u['name']))
        else:
            await typing_delay(event.chat_id)
            await event.reply("Welcome! 🏛️ Before we move at high speed, what's your name? 🤝")
        return

    if u['step'] == 1 and any(w in msg for w in ['a', 'proceed', 'yes']):
        u['step'] = 2
        await typing_delay(event.chat_id)
        await event.reply(get_funnel_text(2, u['type']))
    elif u['step'] == 2 and any(w in msg for w in ['yes', 'ok', 'ready']):
        u['step'] = 3
        await typing_delay(event.chat_id)
        await event.reply(get_funnel_text(3, u['type']))
    elif u['step'] == 3:
        u['dream'] = event.text
        u['step'] = 4
        await typing_delay(event.chat_id)
        await event.reply(get_funnel_text(4, u['type'], name=u['name'], dream=u['dream']))
    elif u['step'] == 4 and any(w in msg for w in ["yes", "send", "link"]):
        u['step'] = 5
        await typing_delay(event.chat_id)
        await event.reply(get_funnel_text(5, u['type']))
    elif u['step'] == 5 and any(w in msg for w in ["details", "account", "yes"]):
        u['step'] = 6
        await typing_delay(event.chat_id)
        await event.reply(get_funnel_text(6, u['type']))

print("🏛️ J-SYSTEM GHOST V5.0 ONLINE... 👻🏎️💨")
client.start()
client.run_until_disconnected()
