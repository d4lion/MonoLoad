from pytube import YouTube
from typing import Optional
from os import getcwd
from re import sub


audioTagsQuality = {
    "48kbps": 139,
    "128kbps": 140,
    "50kbps": 249,
    "70kbps": 250,
    "160kbps": 251
}

# Se toma el directorio de trabajo actual
cwd = getcwd()


# Haciendo uso de los caracteres se toman los ultimos 27 para quedar en la carpeta raiz del proyecto


def download_audio(video: YouTube,
                   resolution: Optional[str] = '128kbps',
                   video_title: Optional[str] = '',
                   out_path: Optional[str] = f'{cwd}/downloads/audios') -> str:
    quality = audioTagsQuality.get(resolution)
    try:
        stream = video.streams.get_by_itag(quality)
        if video_title == '':
            title = stream.title
            clean_title = title.lower()
            clean_title = sub(r"[^\w\s-]", "", clean_title)

            video_title = clean_title

        dowload_path = stream.download(output_path=out_path, filename=f'{
                                       video_title} - {resolution}.mp3')
        return dowload_path

    except Exception as e:
        print(e)


def get_audio_resolution(url: str) -> tuple:
    """
    :param url:
        receives as a parameter the url of some YouTube video of which you want to
        know the audio qualities it has, in addition to obtaining its YouTube type object



    This function is called for the purpose of obtaining the video object: YouTube,
    In addition to having the resolutions of the video you want to download, this only
    will return two values in the form of a tuple.

     resolutions: list
     video: YouTube

     :returns: (resolutions[list], video[YouTube])

    :rtype: tuple
    """
    video = YouTube(url)
    stream_data = video.streams.filter(only_audio=True)
    resolutions = [stream.abr for stream in stream_data]
    return resolutions, video
