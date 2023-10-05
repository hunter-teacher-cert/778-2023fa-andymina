import pandas as pd
from sodapy import Socrata

client = Socrata("data.ny.gov", app_token=None)
df = pd.DataFrame.from_records(client.get("qfsu-zcpv"))

city = input("City: ")
city_df = df[df['city'] == city]
print(f"phone: {city_df['phone_number'].iloc[0]}")
# google maps URL isn't available through this API