import pandas as pd
from sodapy import Socrata
import espeak

espeak.init()
client = Socrata("data.ny.gov", app_token=None)
df = pd.DataFrame.from_records(client.get("55zc-sp6m"))
speaker = espeak.Espeak()

speaker.say("Enter county")
county = input('County: ').upper()
county_df = df[df['county_of_indictment'] == county]
crime_age_df = county_df[['most_serious_crime', 'current_age']]
print(crime_age_df)
speaker.say(crime_age_df.to_string())
print(len(crime_age_df.index))
speaker.say(len(crime_age_df.index))

speaker.say("Enter age")
age = input('Age: ')
age_df = df[df['current_age'] >= age]

min_count = df[df['facility_security_level'] == 'MINIMUM SECURITY']
min_count = len(min_count.index)
age_at_min = age_df[age_df['facility_security_level'] == 'MINIMUM SECURITY']
age_at_min = len(age_at_min.index)

print(f"{age_at_min} at MINIMUM of {min_count} - {age_at_min/min_count * 100}%")
speaker.say(f"{age_at_min} at MINIMUM of {min_count} - {age_at_min/min_count * 100}%")

med_count = len(df[df['facility_security_level'] == 'MEDIUM SECURITY'].index)
age_at_med = len(age_df[age_df['facility_security_level'] == 'MEDIUM SECURITY'].index)
print(f"{age_at_med} at MEDIUM of {med_count} - {age_at_med/med_count * 100}%")
speaker.say(f"{age_at_med} at MEDIUM of {med_count} - {age_at_med/med_count * 100}%")

max_count = len(df[df['facility_security_level'] == 'MAXIMUM SECURITY'].index)
age_at_max = len(age_df[age_df['facility_security_level'] == 'MAXIMUM SECURITY'].index)
print(f"{age_at_max} at MAXIMUM of {max_count} - {age_at_max/max_count * 100}%")
speaker.say(f"{age_at_max} at MAXIMUM of {max_count} - {age_at_max/max_count * 100}%")