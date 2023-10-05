import pandas as pd
import imutils
import cv2

# read the json into a df
url = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
df = pd.read_json(url, lines=True)

# iloc here to grab the first row within that col
img = imutils.url_to_image(df['url'].iloc[0])
cv2.imshow(df['title'].iloc[0] + ' ' + str(df['date'].iloc[0]), img)
cv2.waitKey(0)