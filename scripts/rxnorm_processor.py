import polars as pl
from pathlib import Path
import pandas as pd 

# Reading in the RXNATOMARCHIVE.RRF file
file_path = Path("/Users/amykim/Documents/Health-Informatics/Fall-2025/medical-codex-pipeline/input/RXNATOMARCHIVE.RRF")
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]
# Reading the file with specified options
df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True)

# creating a smaller version of the dataframe with only the columns we need
rxnorm_small = df[['aui', 'str']]
# adding in last updated column
rxnorm_small = rxnorm_small.with_columns([pl.lit('2025-09-09').alias('last_updated')])


# renaming columns to match standard
rxnorm_small = rxnorm_small.rename({
    'aui': 'code',
    'str': 'Description',
    'last_updated': 'LAST_UPDATED'
})

# getting an error message for renaming with "TypeError: DataFrame.rename() got an unexpected keyword argument 'columns'" but fixed with auto suggest and taking out "columns="

output_dir = Path('/Users/amykim/Documents/Health-Informatics/Fall-2025/medical-codex-pipeline/output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE.csv'

rxnorm_small.write_csv(output_path)