import pandas as pd
from sodapy import Socrata

client = Socrata("data.ny.gov", app_token=None)
df = pd.DataFrame.from_records(client.get("8f3n-xj78"))

county = input("County: ")
county_df = df[df['county'] == county]

print(county_df['facility'])
idx = input("Idx: ")

print(county_df["facility"].loc[int(idx)])