##hcpcs_processor.py

import pandas as pd
import logging
import pathlib
import json
import datetime

##path to the input file
file_path = pathlib.Path("/Users/amykim/Downloads/hcpc2025_oct_anweb_corrections_on_v2") 

df = pd.read_txt(file_path)


