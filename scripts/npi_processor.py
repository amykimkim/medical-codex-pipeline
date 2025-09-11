##npi_processor.py

#importing polars for this really big file
import polars as pl

npi_file_path = 'input/npidata_pfile_20050523-20250810.csv'

#only loading in first 1000 rows
df = pl.read_csv(npi_file_path, n_rows=1000)

df_polars = pl.read_csv(npi_file_path)

#lists how many columns there are and what they are = 330 columns
df.columns

#npi will be the code column that represents primary identifier, npi.NPILastName will be the long name/description
df_polars = df_polars.with_columns([
    pl.col("NPI").alias("npi"),
    pl.col("Provider Last Name (Legal Name)").alias("npi.NPILastName")
])

#adding in last updated column
df_polars = df_polars.with_columns([
    pl.lit("2025-09-09").alias("last_updated")
])

df_polars_small = df_polars.select([
    "npi", "npi.NPILastName", "last_updated"
])
print(df_polars_small)

#renaming columns to match standard
df_polars_small = df_polars_small.rename(columns={
    'npi': 'CODE',
    'npi.NPILastName': 'DESCRIPTION',
    'last_updated': 'LAST_UPDATED'
})
print(df_polars_small)

# saving to csv without index
file_output_path = 'output/npi_small.csv '

df_polars_small.write_csv(file_output_path, index = False)

##tried to run this script but got memory error because file is too big
##looked up how to fix this issue but it seems to just be a limitation of my computer