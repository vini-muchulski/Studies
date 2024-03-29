import requests
from bs4 import BeautifulSoup

playlist_url = "https://www.youtube.com/playlist?list=PL43rmSaaxB4qKtx1o5NxY19KQ3PjSbhQw"  # Replace with your playlist URL

response = requests.get(playlist_url)
soup = BeautifulSoup(response.content, "html.parser")


video_links = []
for video_item in soup.find_all( class_="style-scope ytd-playlist-video-list-renderer"):
    print(video_item + " ---")
    
    
    video_link = video_item.find("a", class_="yt-simple-endpoint style-scope ytd-playlist-video-renderer")["href"]
    video_links.append(video_link)
    

print(video_links)