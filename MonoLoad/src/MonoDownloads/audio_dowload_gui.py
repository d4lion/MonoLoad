from pytube import YouTube
from os import getcwd, rename, path

audio_itags_quality = {
    "48kbps" : "139",
    "128kbps" : "140",
    "50kbps" : "249",
    "70kbps" : "250",
    "160kbps" : "251"
}


def dowload(video: YouTube, resolution: str, out_path=f"{getcwd()}/downloads/audios") -> None:
    try:
        stream = video.streams.get_by_itag(audio_itags_quality.get(resolution))
        stream.download(output_path=out_path)
    except Exception as e:
        print(e)


def get_resolution(url: str) -> tuple:
    video = YouTube(url)
    stream_data = video.streams.filter(only_audio=True)
    resolutions = [stream.abr for stream in stream_data]

    return resolutions, video

x = get_resolution('https://www.youtube.com/watch?v=Gm3xyY-o95Q')
dowload(x[1], x[0][1])