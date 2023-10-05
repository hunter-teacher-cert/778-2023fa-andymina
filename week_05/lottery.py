#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.ny.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.ny.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
# user_date = input('enter date (yyyy-mm-dd): ')
# formatted_date = f"{user_date}T00:00:00.000"
results = client.get(f"6nbc-h7bj", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

user_date = input('enter date (yyyy-mm-dd): ')
formatted_date = f"{user_date}T00:00:00.000"
print(results_df[results_df['draw_date'] == formatted_date])