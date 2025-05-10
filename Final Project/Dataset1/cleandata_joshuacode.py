from googletrans import Translator
import pandas as pd

translator = Translator()

# read the CSV file into a pandas dataframe
df = pd.read_csv('movies.csv')
print(df.head())

#japanese_films = df[df['original_language'] == 'ja']
films_to_translate = df[(df['original_language'] != 'en') & (df['original_language'] != '0') & (df['original_language'] != '6')]
print(films_to_translate.head())

translated_df = df[df['original_language'] == 'en']

for index, row in films_to_translate.iterrows():
    # step 1: tramsalte the title name
    translated_title_name = translator.translate(row['original_title'], dest='en').text
    #step 2: add original unstranslated row to the translated df
    original_row = df.loc[index]
    translated_df = translated_df.append(original_row, ignore_index=True)    
    # Step 3: Update the recently added row's original_title with the translated title name
    translated_df.at[index, 'original_title'] = translated_title_name

translated_df.to_csv('translated.csv', index=False)
