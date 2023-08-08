# import scrapetube
# from pytube import YouTube
# from pytube.exceptions import AgeRestrictedError, VideoUnavailable
# import threading


# error = []


# def getVideoID(channelURL, content_type):
#     videoId = []
#     try:
#         videos = scrapetube.get_channel(channel_url = channelURL, content_type = content_type)
#         for video in videos:
#             videoId.append(video['videoId'])
#         return videoId
#     except Exception as e:
#         print("Youtub Channel link does not exists")
#         exit()
    

# def downloadVideo(link):
#     try:
#         youtubeObject = YouTube(link)
#         youtubeObject = youtubeObject.streams.get_highest_resolution()
#         youtubeObject.download('Downloads')
#     except Exception as e:
#         print(f"{link} :Error {e}")
#         error.append(f"{link} :Error {e}")
#     print(f"Download {link} is completed successfully")


# def threadTask(lists):
#     for i in range(0, len(lists), 10): 
#         yield lists[i:i + 10]

# def threadDownload(lists):
#     for i in range(0, len(lists)):
#         # print(i)
#         downloadVideo('http://youtube.com/watch?v=' + lists[i])

# def executeThread(videoID_list):
#     thread_list = []

#     for i in range(0, len(videoID_list)):
#         thread = threading.Thread(target=threadDownload, args=(videoID_list[i],))
#         thread_list.append(thread)
#         thread.start()
    
#     for i in thread_list:
#         i.join()

    


    
    
# if __name__ =="__main__":

#     while 1:

#         link = str(input('Youtube Channel URL: '))

#         while (link == ''):
#             link = str(input('Youtube Channel URL: '))


#         videoID = getVideoID(link, 'shorts')

#         videoID_list = list(threadTask(videoID))

#         executeThread(videoID_list)
        
#         print("--------------------------------------------------------------------------")

######################################################################################################################
# from bs4 import BeautifulSoup
# import requests
# import json

# url = "https://www.youtube.com/@mojiko.official/shorts"

# res = requests.get(url)
# res.encoding = "utf-8"

# # if res.status_code == 200:
# #     print("Successful")
# # elif res.status_code == 404:
# #     print("Error 404 page not found")
# # else:
# #     print("Not both 200 and 404")

# temp = ""
# soup = BeautifulSoup(res.text, "html.parser")
# text = soup.findAll('script')

# for i in text[35]:
#     temp = i

# temp = temp.rsplit('var ytInitialData = ')
# temp2 = temp[1].rsplit(';', 1)

# json_obj = json.loads(temp2[0])

# youtube_content = json_obj['contents']['twoColumnBrowseResultsRenderer']['tabs'][2]['tabRenderer']['content']['richGridRenderer']['contents']

# for i in youtube_content:
#     try:
#         print(i['richItemRenderer']['content']['reelItemRenderer']['videoId'])
#         print(i['richItemRenderer']['content']['reelItemRenderer']['headline']['simpleText'])
#         print(i['richItemRenderer']['content']['reelItemRenderer']['thumbnail']['thumbnails'][0]['url'])
#     except:
#         continue