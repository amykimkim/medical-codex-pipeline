# icd10cm_processor.py

import pandas as pd
import re

#define the file path
file_path = 'input/icd10cm_order_2025.txt'

# blank list to hold parsed codes
codes = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:

        #removing whitespace and checking line length
        line = line.rstrip('/n/r')
        if len(line) <15:
            continue

        #parse the fixed-length format
        order_num = line[0:5].strip()
        code = line[6:13].strip()
        level = line[14:15].strip()

        #parse description and detailed description that follows
        remaining_text = line[1:]

        #Split by 4+ consecutive spaces to separate description from detailed description
        parts = re.split(r'\s{4,}', remaining_text, 1)

        #extract description and description_detailed
        description = parts[0].strip() if len(parts) > 0 else ""
        description_detailed = parts[1].strip() if len(parts) > 1 else ""

        #append the parsed data to codes list
        codes.append({
            'order_num': order_num,
            'code': code,
            'level': level,
            'description': description,
            'description_detailed': description_detailed
        })
#only including columns we need: code and description_detailed
icd10us_small = pd.DataFrame(codes)[['code', 'description_detailed']]

#adding in last updated column
icd10us_small['Last_updated'] = '2025-09-10'

#print columns to see what was parsed
print(icd10us_small)

#file output path
file_output_path = 'output/icd10cm_us_small.csv'
icd10us_small.to_csv(file_output_path, index = False)