import argparse

from src.MonoDownloads import video_download as video
from src.MonoDownloads import audio_download as audio
from src.MultiDownloads import video_downloads as multiVideo
from src.MultiDownloads import audio_downloads as multiAudio
from colorama import Fore, init

SUCCESS = 0


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
    parser.add_argument('-m', '--multidownload', type=bool, default=False)
    parser.add_argument('-df', '--datafile', type=str, default='urls.txt')
    parser.add_argument('-t', '--threads', default=2, type=int)
    parser.add_argument('-vq', '--videoquality', choices=['1080p', '720p', '480p', '360p', '240p', '144p'],
                        default='480p')
    parser.add_argument('-aq', '--audioquality', choices=['48kbps', '128kbps', '50kbps', '70kbps', '160kbps'],
                        default='128kbps')

    args = parser.parse_args()

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

    def multiDownload(format: str, file_name: str, threads: int, video_quality: str, audio_quality: str):
        # format_download = input("\n Do you want to download mp3 or mp4 files?: ")

        url = list()

        with open(file_name, 'r') as f:
            videos_url = [line.split('\n') for line in f]
            for url_video in videos_url:
                url.append(url_video[0])

        match format:
            case 'video':
                multiVideo.download(videos_url=url, threads=threads, quality=video_quality, filename=file_name)

            case 'audio':
                multiAudio.download(audios_url=url, threads=threads, quality=audio_quality)

    if args.multidownload:
        multiDownload(format=args.format, file_name=args.datafile, threads=args.threads,
                      video_quality=args.videoquality, audio_quality=args.audioquality)
        return SUCCESS
    else:
        monoDownload()
        return SUCCESS


if __name__ == "__main__":
    main()
