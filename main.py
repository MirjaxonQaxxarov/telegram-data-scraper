from telethon.sync import TelegramClient
import pandas as pd

# API ma'lumotlari
API_ID = 'api_id'  # API_ID ni o'zingizning haqiqiy API_ID bilan almashtiring
API_HASH = 'api_hash'  # API_HASH ni o'zingizning haqiqiy API_HASH bilan almashtiring
CHANNEL_USERNAME = 'channel_username'  # @ belgisiz kanal username yoki ID

# Telethon sessiyasini yaratish
with TelegramClient('my', API_ID, API_HASH) as client:
    messages = []
    
    # Kanal postlarini olish
    for message in client.iter_messages(CHANNEL_USERNAME):
        print(len(messages))
        text = message.message
        if text:
            messages.append([message.date.strftime('%Y-%m'), text.replace('\n', ' ')])


    # CSV ga saqlash
    df = pd.DataFrame(messages, columns=['date', 'post_text'])
    df.to_csv(f'csv2/{CHANNEL_USERNAME}.csv', index=False, encoding='utf-8')

print(f"Barcha postlar muvaffaqiyatli saqlandi: {CHANNEL_USERNAME}.csv")
