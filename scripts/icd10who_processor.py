# icd10who_processor.py

import pandas as pd

# Reading in the ICD-10-WHO file
file_path = '/Users/amykim/Documents/Health-Informatics/Fall-2025/medical-codex-pipeline/input/icd102019syst_codes.txt'
columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(file_path, sep=';', header=None, names=columns)

# checking the dataframe
first_10_columns = df.columns[:10]

#print data with just first 10 columns and all rows to see what is relevant
print(df[first_10_columns])

# creating a smaller version of the icd10who dataframe with only the columns we need
icd10who_small = df[['icd10_code', 'title_en']]

#renaming columns to match standard
icd10who_small = icd10who_small.rename(columns=
    {'icd10_code': 'CODE',
    'title_en': 'DESCRIPTION'}
)

#adding in last updated column
icd10who_small['LAST_UPDATED'] = '2025-09-10'

# saving to csv without index
file_output_path = 'output/icd10who_small.csv'

icd10who_small.to_csv(file_output_path, index = False)
print(icd10who_small)