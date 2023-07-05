from os import getcwd
from .itags import audio_itags_quality
from pytube import YouTube, streams
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor




init(autoreset=False)

def multi_download(url: str, quality:str , out_path:str):
    video = YouTube(url)
    quality_to_itag = audio_itags_quality.get(quality)
    stream = video.streams.get_by_itag(quality_to_itag)
    stream.download(output_path=out_path)
    print(f"{Fore.GREEN}Succesfully downloaded: {video.title}")


def download(audios_url: list, quality="128kbps", threads=2, out_path=f"{getcwd()}/downloads/audios"):
    """
    Variables
    ---------
    * audios_url (list): The list to be provided must be given in text file format with .txt extension must contain all urls separated by the enter key

    * quality (str): the quality variable can choose a range in which the audios with the different qualities will be downloaded
    
    * threads (int): With this, the aim is to provide the number of threads with which you want to work in the simultaneous download of the different audios
    
    * out_path (str): In this variable, the proportional folder is searched for where the download folder with the audios is to be stored.

    """


    with ThreadPoolExecutor(max_workers=threads) as executor:
        for url in audios_url:
            executor.submit(multi_download, url=url, quality=quality, out_path=out_path)