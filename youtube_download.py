from pytube import YouTube
link = input("enter link:")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()