import scrapetube

videos = scrapetube.get_channel(channel_url='https://www.youtube.com/@mojiko.official', content_type='shorts')

for video in videos:
    print(video)