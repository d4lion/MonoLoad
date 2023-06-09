from src.MonoDownloads import video_download as video
from src.MonoDownloads import audio_download as audio
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
    print(Fore.CYAN + MonoLoad)
    url = input(Fore.YELLOW + "Type the url you want to dowload: " + Fore.WHITE) 

    format_download = input("\n Do you want to download mp3 or mp4 fille?: ")

    if format_download == "mp3":
        audio.download(url)
    else:
        video.download(url)




if __name__ == "__main__":
    main()