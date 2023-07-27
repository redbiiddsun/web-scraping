import scrapetube
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError, VideoUnavailable
import threading
import concurrent.futures


error = []


def getVideoID(channelURL, content_type):
    videoId = []
    videos = scrapetube.get_channel(channel_url='https://www.youtube.com/@mojiko.official', content_type='shorts')
    for video in videos:
        videoId.append(video['videoId'])
    return videoId

def downloadVideo(link):
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()
    except:
        print("An error has occurred")
        error.append(link)
    print("Download is completed successfully")


# for i in range(0, len(list)): 
#     downloadVideo('http://youtube.com/watch?v=' + list[i])

def jobPrepare(lists):
    for i in range(0, len(lists), 10): 
        yield lists[i:i + 10]

def threadDownload(lists):
    for i in range(0, len(lists)):
        print(i)
        downloadVideo('http://youtube.com/watch?v=' + lists[i])

# def createThread(list):
    

if __name__ =="__main__":
    lists = getVideoID("channelURL", "content_type")

    x = list(jobPrepare(lists))

    # # # creating thread
    # t1 = threading.Thread(target=threadDownload, args=(x[0],))
    # t2 = threading.Thread(target=threadDownload, args=(x[1],))
 
    # # # starting thread 1
    # t1.start()
    # # # starting thread 2
    # t2.start()
 
    # # # wait until thread 1 is completely executed
    # t1.join()
    # # # wait until thread 2 is completely executed
    # t2.join()
 
    # # # both threads completely executed
    # print("Done!")

    thread_list = []
    for i in range(0, len(x)):
        thread = threading.Thread(target=threadDownload, args=(x[i],))
        thread_list.append(thread)
        thread.start()