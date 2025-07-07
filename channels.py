from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
import pandas as pd
from const import API_HASH, API_ID


chat_ids_df = pd.read_csv('chat_data.csv')
CHANELS = chat_ids_df['username'].tolist()

with TelegramClient('my', API_ID, API_HASH) as client:
    for channel in CHANELS:
        messages = []
        try:
            for message in client.iter_messages(channel):
                text = message.message
                if text:
                    messages.append([message.date.strftime('%Y-%m'), text.replace('\n', ' ')])
                    print([message.date.strftime('%Y-%m'), text.replace('\n', ' ')])
            if messages:
                df = pd.DataFrame(messages, columns=['date', 'post_text'])
                df.to_csv(f'csv2/{channel}.csv', index=False, encoding='utf-8')
                print(f"Barcha postlar muvaffaqiyatli saqlandi: {channel}.csv")
                
                chat_ids_df = chat_ids_df[chat_ids_df['username'] != channel]
                chat_ids_df.to_csv('chat_data.csv', index=False)
                print(f"{channel} chat_data.csv dan o'chirildi.")
            else:
                print(f"{channel} uchun hech qanday post topilmadi.")
        except Exception as e:
            print(f"{channel} error: {e}")
