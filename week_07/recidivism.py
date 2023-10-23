import pandas as pd
from sodapy import Socrata
import espeak

espeak.init()
client = Socrata('data.ny.gov', app_token=None)
df = pd.DataFrame.from_records(client.get('y7pw-wrny'))
speaker = espeak.Espeak()

speaker.say("Enter county")
x = input("...pause...")
county = input('County: ').upper()
county_df = df[df['county_of_indictment'] == county]
not_returned = len(county_df[county_df['return_status'] == 'Not Returned'])
print(f"{not_returned} not returned - {not_returned/len(county_df) * 100}%")
speaker.say(f"{not_returned} not returned - {not_returned/len(county_df) * 100}%")
x = input("...pause...")

speaker.say("Enter age")
x = input("...pause...")
age = int(input('Age: '))
age_df = df[df['age_at_release'].astype(int) <= age]

new_offense_count = len(age_df[age_df['return_status'] == 'New Felony Offense'])
print(f"new felony offense - {new_offense_count}")
speaker.say(f"new felony offense - {new_offense_count}")
x = input("...pause...")

parole_vio_count = len(age_df[age_df['return_status'] == 'Returned Parole Violation'])
print(f"returned parole violation - {parole_vio_count}")
speaker.say(f"returned parole violation - {parole_vio_count}")
x = input("...pause...")
