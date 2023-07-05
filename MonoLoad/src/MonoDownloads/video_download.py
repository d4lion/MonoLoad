from os import getcwd
from tqdm import tqdm
from time import sleep

from pytube import YouTube, streams
from .itags import videos_itags_resolution as video_itags
from colorama import init, Fore


init(autoreset=True)

def download(url, out_path=f"{getcwd()}/downloads/videos"):
    
    def progress(stream, data_chunk, bytes_remaing ):
        bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt} {postfix}'
        bar = tqdm(total=stream.filesize, bar_format=bar_format)
        bar.update(stream.filesize - bytes_remaing)

    def dowload_by_resolution(resolutions, video):
       print(f"\n video title: {Fore.RED + video.title} \n {Fore.WHITE} \n qualities: {resolutions}")

       video_quality_dowload = input("\n Type the quality: ")
       return video_quality_dowload

    def get_resolutions(stream_data):
        resolutions = list()

        for data in stream_data:
            resolutions.append(data.resolution)

        resolutions = list(filter(lambda x: x is not None, set(resolutions)))
        return resolutions
    


    video = YouTube(url)
    stream_data = video.streams.filter(file_extension="mp4")
    resolutions = get_resolutions(stream_data)

    video_quality_to_dowload = dowload_by_resolution(resolutions=resolutions, video=video)

    stream = video.streams.get_by_itag(video_itags.get(video_quality_to_dowload))
    stream.download(output_path=out_path)