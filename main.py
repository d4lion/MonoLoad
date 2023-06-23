import argparse

from src.MonoDownloads import video_download as video
from src.MonoDownloads import audio_download as audio
from src.MultiDownloads import video_downloads as multiVideo
from src.MultiDownloads import audio_downloads as multiAudio
from colorama import Fore, init



def main():

    init(autoreset=True)

    MonoLoad = """
    __  __                   _                     _ 
    |  \/  |                 | |                   | |
    | \  / | ___  _ __   ___ | |     ___   __ _  __| |
    | |\/| |/ _ \| '_ \ / _ \| |    / _ \ / _` |/ _` |
    | |  | | (_) | | | | (_) | |___| (_) | (_| | (_| |
    |_|  |_|\___/|_| |_|\___/|______\___/ \__,_|\__,_|
    """
    print(Fore.CYAN + MonoLoad)


    parser = argparse.ArgumentParser()
    
    parser.add_argument('-f', '--format', choices=['video', 'audio'], default='video')
    parser.add_argument('-m', '--multidownload', type=str, default='urls.txt')
    parser.add_argument('-t', '--threads', default=2, type=int)
    parser.add_argument('-q', '--quality', choices=['1080p', '720p', '480p', '360p', '240p', '144p'], default='480p')




    def monoDownload():
        url = input(Fore.YELLOW + "Type the url you want to dowload: " + Fore.WHITE) 

        format_download = input("\n Do you want to download mp3 or mp4 fille?: ")

        if format_download == "mp3":
            audio.download(url)
        elif format_download == "mp4":
            video.download(url)
        else:
            print("Select a correct option.")
            return monoDownload()

    def multiDownload(format, file_name, threads, quality):
        # format_download = input("\n Do you want to download mp3 or mp4 files?: ")

        url = list()

        with open(file_name, 'r') as f:
            videos_url = [line.split('\n') for line in f]
            for url_video in videos_url:
                url.append(url_video[0])
                    
        """
        TODO: Permitir que la funcion de MultiDowload tanto en video como en audio permita el uso de lo parametros format, threads, quality para mejorar la experiencia de uso mediante la terminal 
        """
        print("Hello World")
        multiAudio.download(url)

    

    args = parser.parse_args()
    print(args)
    multiDownload(format=args.format, file_name=args.multidownload, threads=args.threads, quality=args.quality)



if __name__ == "__main__":
    main()