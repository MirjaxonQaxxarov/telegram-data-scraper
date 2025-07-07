import pandas as pd
import re

def extract_car_details(text):
    details = {}
    
    model_match = re.search(r'🚘Moshina modeli: (.+?) 🔢Pozitsiya:', text)
    details['model'] = model_match.group(1) if model_match else None
    details['pozitsiya'] = re.search(r'Pozitsiya: (.+?) ', text)
    details['narx'] = re.search(r'Narxi: ([\d,]+\$)', text)
    details['yil'] = re.search(r'Yil: (\d{4})', text)
    details['km'] = re.search(r'Probeg: ([\d,.]+) km', text)
    details['yonilgi'] = re.search(r'⛽️(.*?)💲', text)
    details['kraska'] = re.search(r'Kraska: (\d+%)', text)
    details['rang'] = re.search(r'Rangi: (\S+)', text)
    details['hudud'] = re.search(r'🚩 (.+?) ✅', text)
    
    for key, value in details.items():
        details[key] = value.group(1) if isinstance(value, re.Match) else value
    
    # if None in details.values():
    #     return None
    none_count = sum(1 for v in details.values() if v is None)
    if none_count > 2:
        return None
    return details

# CSV faylni yuklash
df = pd.read_csv("csv/Yutouz_avto.csv")

# Har bir post uchun ma'lumotlarni ajratib olish
data = []
for _, row in df.iterrows():
    details = extract_car_details(row['post_text'])
    if details:
        details['posted_date'] = row['date']
        data.append(details)


car_df = pd.DataFrame(data)

car_df.to_csv("default/extracted_cars.csv", index=False)
print(car_df.head())
