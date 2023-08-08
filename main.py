import scrapetube
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError, VideoUnavailable
import threading


error = []


def getVideoID(channelURL, content_type):
    videoId = []
    try:
        videos = scrapetube.get_channel(channel_url = channelURL, content_type = content_type)
        for video in videos:
            videoId.append(video['videoId'])
        return videoId
    except Exception as e:
        print("Youtub Channel link does not exists")
        exit()
    

def downloadVideo(link):
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download('Downloads')
    except Exception as e:
        print(f"{link} :Error {e}")
        error.append(f"{link} :Error {e}")
    print(f"Download {link} is completed successfully")


def threadTask(lists):
    for i in range(0, len(lists), 10): 
        yield lists[i:i + 10]

def threadDownload(lists):
    for i in range(0, len(lists)):
        downloadVideo('http://youtube.com/watch?v=' + lists[i])

def executeThread(videoID_list):
    thread_list = []

    for i in range(0, len(videoID_list)):
        thread = threading.Thread(target=threadDownload, args=(videoID_list[i],))
        thread_list.append(thread)
        thread.start()
    
    for i in thread_list:
        i.join()

if __name__ =="__main__":

    while 1:

        link = str(input('Youtube Channel URL: '))

        while (link == ''):
            link = str(input('Youtube Channel URL: '))


        videoID = getVideoID(link, 'shorts')

        videoID_list = list(threadTask(videoID))

        executeThread(videoID_list)

        print("--------------------------------------------------------------------------")
        print("Error Report")
        print(f"There are {len(error)} would you like to continue? ()")
        print("--------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------")
