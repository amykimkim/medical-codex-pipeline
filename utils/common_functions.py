import pandas as pd

def save_to_formats(df: pd.DataFrame, base_filename: str):
    csv_path = f"{base_filename}.csv"
    df.to_csv(csv_path, index = False)

