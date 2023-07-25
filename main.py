from bs4 import BeautifulSoup
import requests
import json

url = "https://www.youtube.com/@mojiko.official/shorts"

res = requests.get(url)
res.encoding = "utf-8"

# if res.status_code == 200:
#     print("Successful")
# elif res.status_code == 404:
#     print("Error 404 page not found")
# else:
#     print("Not both 200 and 404")

temp = ""
soup = BeautifulSoup(res.text, "html.parser")
text = soup.findAll('script')

for i in text[35]:
    temp = i

temp = temp.rsplit('var ytInitialData = ')
temp2 = temp[1].rsplit(';', 1)

json_obj = json.loads(temp2[0])

youtube_content = json_obj['contents']['twoColumnBrowseResultsRenderer']['tabs'][2]['tabRenderer']['content']['richGridRenderer']['contents']

for i in youtube_content:
    try:
        print(i['richItemRenderer']['content']['reelItemRenderer']['videoId'])
        print(i['richItemRenderer']['content']['reelItemRenderer']['headline']['simpleText'])
        print(i['richItemRenderer']['content']['reelItemRenderer']['thumbnail']['thumbnails'][0]['url'])
    except:
        continue


