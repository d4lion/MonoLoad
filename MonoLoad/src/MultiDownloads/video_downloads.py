from os import getcwd, path
from .itags import videos_itags_resolution
from pytubefix import YouTube, streams
from colorama import init, Fore
from concurrent.futures import ThreadPoolExecutor

# Auto reset color in colorama
init(autoreset=True)

CWD = getcwd()

def multi_download(url: str, quality:str ,out_path: str) -> None:
    video = YouTube(url)
    stream = video.streams.get_by_itag(videos_itags_resolution.get(quality))
    stream.download(output_path=out_path, filename=f"{video.title}.mp4")
    print(f"{Fore.GREEN}Succesfully downloaded: {video.title}")



def download(videos_url: list, threads: int , quality: str , filename: str ,out_path=None) -> None:
    """Download multiple videos concurrently"""
    if out_path is None:
        out_path = path.join(getcwd(), "downloads", "videos")
        
    # Send in a pool Threads the videos url to download
    with ThreadPoolExecutor(threads) as executor:
        for url in videos_url:
            executor.submit(multi_download, url=url, quality=quality, out_path=out_path)
