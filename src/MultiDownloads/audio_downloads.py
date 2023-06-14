from pytube import YouTube, streams
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor



init(autoreset=False)



def multi_download(url: str, out_path="downloads/audios"):
    video = YouTube(url)
    stream = video.streams.get_by_itag('140')
    stream.download(output_path=out_path)
    print(f"{Fore.GREEN}Succesfully downloaded: {video.title}")


def download(audios_url: list):
    # Send taskt to the threads pool
    with ThreadPoolExecutor(max_workers=4) as executor:
        for url in audios_url:
            executor.submit(multi_download, url)