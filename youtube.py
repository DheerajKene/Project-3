
from pytube import YouTube
def audio_from_youtube(url):
    yt = YouTube(url)
    aud = yt.streams.filter(only_audio=True).first()
    aud.download()
video_url = input("Enter youtube url: ")
audio_from_youtube(video_url)