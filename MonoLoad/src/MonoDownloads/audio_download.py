from pytube import YouTube, streams, StreamQuery, Stream
from colorama import init, Fore
from .itags import audio_itags_quality
from os import getcwd, rename, listdir, path
from typing import NoReturn, Required, Optional
from re import sub

init(autoreset=True)

def download(url: Required[str], out_path: Optional[str] = f"{getcwd()}/downloads/audios") -> NoReturn:

    def get_resolution(streams_data: StreamQuery) -> list[str]:
        resolutions = list()

        for stream in streams_data:
            resolutions.append(stream.abr)

        return resolutions
    
    def audio_quality_download(resolutions: Required[list[str]], video) -> str:
        print(f"\n video title: {Fore.RED + video.title} \n {Fore.WHITE} \n qualities: {resolutions}")

        audio_quality_to_download: str = input("\n Type the quality: ")

        return audio_quality_to_download 

    try:
        video = YouTube(url)
        streams_data = video.streams.filter(only_audio=True)
        resolutions: list[str] = get_resolution(streams_data=streams_data)
        audio_qulity_to_dowload = str()

        while audio_qulity_to_dowload not in resolutions:
            audio_qulity_to_dowload = audio_quality_download(resolutions=resolutions, video=video)

        stream: Stream = video.streams.get_by_itag(audio_itags_quality.get(audio_qulity_to_dowload))

        title: str = video.title
        clean_title: str = title.lower()
        clean_title = sub(r"[^\w\s-]", "", clean_title)

        title = clean_title

        stream.download(output_path=out_path, skip_existing=True, filename=f"{title}.mp3")
        #fix_extensions(out_path=out_path, song_name=title)
    except Exception as e:
        print(f"\n {e} \n Check the video url and try again.")
