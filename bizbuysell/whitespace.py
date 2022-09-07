# import csv

# with open('/home/stephen/Documents/web-scraping/web-scrapers/bizbuysell/details.csv', 'r') as f:
#     raw_csv = f.read()
#     clean_csv = raw_csv.strip(' ')
    
# with open('details_clean.csv', 'w') as f:
#     f.write(clean_csv)

import pandas as pd
import numpy as np


df = pd.read_csv('details.csv', quotechar='"')

# for each column
for col in df.columns:
    # check if the columns contains string data
    if pd.api.types.is_string_dtype(df[col]):
        df[col] = df[col].str.strip(' \r\n')
# df = df.replace({"":np.nan}) # if there remained only empty string "", change to Nan
print(df)


df.to_csv('details_clean.csv')