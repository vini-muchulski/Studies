from pytube import YouTube
import wget

#url = "https://www.youtube.com/watch?v=QdBZY2fkU-0&pp=ygUOcm9ja3N0YXIgZ2FtZXM%3D"
url = "https://www.youtube.com/watch?v=I8LFZydzQW4&list=RDI8LFZydzQW4&start_radio=1"
video = YouTube(url)


#titulo do video
print(video.title)

#thumbnail do video
print(video.thumbnail_url)
#wget.download(video.thumbnail_url)
#baixar video

video.streams.get_highest_resolution().download()

for resolucao in video.streams:
    print(resolucao)