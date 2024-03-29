links = []

with open("videos.txt" ,"r") as file:
    for linha in file:
        links.append(linha.strip())
        
for link in links:
    print(link)
    
    
"""
#baixar video
video.streams.get_highest_resolution().download()

for resolucao in video.streams:
    #print(resolucao)
    pass
    
"""
#thumbnail do video
#print(video.thumbnail_url)
#wget.download(video.thumbnail_url)