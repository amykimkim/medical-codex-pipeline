##loinc_processor.py

import pandas as pd

loinc = pd.read_csv('input/Loinc.csv')

# typed loinc.info() to see all columns

# loinc_num will be the code column that represents primary identifier, loinc.COMPONENT will be the long name/description
loinc.LOINC_NUM
print(loinc.LOINC_NUM)

loinc.LONG_COMMON_NAME
print(loinc.LONG_COMMON_NAME)


# creating a smaller version of the loinc dataframe with only the columns we need
loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
print(loinc_small)

#adding in last updated column
loinc_small['last_updated'] = '2025-09-08'
print(loinc_small)

#renaming columns to match standard
loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'CODE',
    'LONG_COMMON_NAME': 'DESCRIPTION',
    'last_updated': 'LAST_UPDATED'
})

# saving as csv without index
file_output_path = 'output/loinc_small.csv'

loinc_small.to_csv(file_output_path, index = False)
print(loinc_small)