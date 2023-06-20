from src.MonoDownloads import video_download as video
from src.MonoDownloads import audio_download as audio

from src.MultiDownloads import video_downloads as multiVideo
from src.MultiDownloads import audio_downloads as multiAudio
from colorama import Fore, init

init(autoreset=True)

MonoLoad = """
  __  __                   _                     _ 
 |  \/  |                 | |                   | |
 | \  / | ___  _ __   ___ | |     ___   __ _  __| |
 | |\/| |/ _ \| '_ \ / _ \| |    / _ \ / _` |/ _` |
 | |  | | (_) | | | | (_) | |___| (_) | (_| | (_| |
 |_|  |_|\___/|_| |_|\___/|______\___/ \__,_|\__,_|
"""


def main():

    def monoDownload():
        print(Fore.CYAN + MonoLoad)
        url = input(Fore.YELLOW + "Type the url you want to dowload: " + Fore.WHITE) 

        format_download = input("\n Do you want to download mp3 or mp4 fille?: ")

        if format_download == "mp3":
            audio.download(url)
        elif format_download == "mp4":
            video.download(url)
        else:
            print("Select a correct option.")
            return monoDownload()

    def multiDownload():
        # format_download = input("\n Do you want to download mp3 or mp4 files?: ")
        url = list()

        with open('videos.txt', 'r') as f:
            videos_url = [line.split('\n') for line in f]
            for url_video in videos_url:
                url.append(url_video[0])
                    
        multiAudio.download(url)

    multiDownload()



if __name__ == "__main__":
    main()