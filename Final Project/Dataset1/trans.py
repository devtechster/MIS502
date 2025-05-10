import csv
from googletrans import Translator

# Create a translator object
translator = Translator()

# Open the CSV file and read the data
with open('movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Iterate through the data and translate the 'original_title' column to English
for row in data:
    original_title = row['original_title']
    translated_title = translator.translate(original_title, dest='en').text
    row['original_title'] = translated_title

# Write the translated data back to the CSV file
with open('filename_translated.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(data)
