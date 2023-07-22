from bs4 import BeautifulSoup
import requests


url = "https://www.youtube.com/@mojiko.official/shorts"

res = requests.get(url)
res.encoding = "utf-8"
print(res)


if res.status_code == 200:
    print("Successful")
elif res.status_code == 404:
    print("Error 404 page not found")
else:
    print("Not both 200 and 404")


soup = BeautifulSoup(res.text, 'html.parser')
text = soup.findAll('script')
print(text[35])
# for i in text: 
    
#     print(i)
#     print("----------------------------------------------------------------------------------------")
