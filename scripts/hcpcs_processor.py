##hcpcs_processor.py

import pandas as pd
import polars as pl

# reading in fixed width file for HCPCS
file_path = 'input/HCPC2025_OCT_ANWEB_v2.txt'
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]

# defining dataframe
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)

# typed df.info() to see descriptions

# creating a smaller file with only the columns we need
hcpcs_small = df[['Code', 'Description1']]

# adding in last updated column
hcpcs_small['last_updated'] = '2025-09-09'


#renaming columns to match standard
hcpcs_small = hcpcs_small.rename(columns={
    'Code': 'CODE',
    'Description1': 'DESCRIPTION',
    'last_updated': 'LAST_UPDATED'
})

# saving as csv file in output folder
output_path = "/Users/amykim/Documents/Health-Informatics/Fall-2025/medical-codex-pipeline/output/hcpcs_small.csv"
hcpcs_small.to_csv(output_path, index=False)
print(hcpcs_small)