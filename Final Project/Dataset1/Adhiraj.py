#pip install googletrans==4.0.0-rc1

from googletrans import Translator
import pandas as pd
import unicodedata

def is_valid_japanese(text):
    for c in text:
        name = unicodedata.name(c, None)
        if name is None or "CJK UNIFIED" not in name and "HIRAGANA" not in name and "KATAKANA" not in name:
            return False
    return True

df = pd.read_csv('movies_ja.csv')

valid_rows = []
for index, row in df.iterrows():
    if is_valid_japanese(row[3]):
        valid_rows.append(row)

valid_df = pd.DataFrame(valid_rows)

valid_df.to_csv('cleaned_filename.csv', index=False)

translator = Translator()

data = pd.read_csv('cleaned_filename.csv')

translations = []

for index, row in data.iterrows():
    japanese_text = row[3]
    translation = translator.translate(japanese_text, src='ja', dest='en').text
    translations.append(translation)

data['english_text'] = translations

data.to_csv('translated_file.csv', index=False)
