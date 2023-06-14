import time

from pytube import YouTube, streams
from colorama import init, Fore
from concurrent.futures import ThreadPoolExecutor

# Auto reset color in colorama
init(autoreset=True)

def multi_download(url: str, out_path="downloads/videos") -> None:
    video = YouTube(url)
    stream = video.streams.get_by_itag('135')
    stream.download(output_path=out_path)
    print(f"{Fore.GREEN}Succesfully downloaded: {video.title}")



def download(videos_url: list, out_path="downloads/videos") -> None:
    # Send in a pool Threads the videos url to download
    with ThreadPoolExecutor(max_workers=4) as executor:
        for url in videos_url:
            executor.submit(multi_download, url)
