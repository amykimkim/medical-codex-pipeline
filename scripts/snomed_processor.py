import polars as pl
from pathlib import Path
import pandas as pd

# Reading in the SNOMED CT Description file but only the first 1000 rows since it was giving me an error message when I tried git push without it saying file was too large 
file_path = Path('/Users/amykim/Documents/Health-Informatics/Fall-2025/medical-codex-pipeline/input/sct2_Description_Full-en_US1000124_20250901.txt', n=1000)

# Reading the file with specified options
df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)
# creating a smaller version of the snomed dataframe with only the columns we need and first 1000 rows since it was giving me an error message when I tried git push without it saying file was too large
snomed_small = df[['id', 'term',]].head(1000)

# adding in last updated column
snomed_small = snomed_small.with_columns([pl.lit('2025-09-09').alias('last_updated')])

# renaming columns to match standard
snomed_small = snomed_small.rename({
    'id': 'code',
    'term': 'Description',
    'last_updated': 'LAST_UPDATED'
})

# creating output path
file_output_path = 'output/snomed_small.csv'

snomed_small.write_csv(file_output_path)
print(snomed_small)

# tried deleting this output file and git pushing the rest of my changes but it still said the file was too large even though it is not in the trash
# tried suggestion of Install Git LFS: but my terminal would not run the commands that were suggested in the instructions
# made sure that the input file is in the .gitignore so it does not get pushed to github
# tried placing the snomed small output file in the .gitignore as well but it still said the file was too large