from os import getcwd, path
from tqdm import tqdm

from pytube import YouTube, streams
from .itags import videos_itags_resolution as video_itags
from colorama import init, Fore


init(autoreset=True)

def download(url, out_path=None):
    if out_path is None:
        out_path = path.join(getcwd(), "downloads", "videos")
    
    def progress(stream, data_chunk, bytes_remaining):
        """Callback for download progress"""
        # Calculate progress
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        
        # Update progress bar
        if not hasattr(progress, 'bar'):
            progress.bar = tqdm(total=total_size, unit='B', unit_scale=True, 
                              desc='Downloading', bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}')
        
        progress.bar.update(len(data_chunk))

    def dowload_by_resolution(resolutions, video):
       print(f"\n video title: {Fore.RED + video.title} \n {Fore.WHITE} \n qualities: {resolutions}")

       video_quality_dowload = input("\n Type the quality: ")
       return video_quality_dowload

    def get_resolutions(stream_data):
        resolutions = set()

        for data in stream_data:
            if data.resolution:
                resolutions.add(data.resolution)

        return sorted(list(resolutions))
    

    video = YouTube(url, on_progress_callback=progress)
    stream_data = video.streams.filter(file_extension="mp4")
    resolutions = get_resolutions(stream_data)

    video_quality_to_dowload = dowload_by_resolution(resolutions=resolutions, video=video)

    stream = video.streams.get_by_itag(video_itags.get(video_quality_to_dowload))
    stream.download(output_path=out_path)
    
    # Close progress bar if it exists
    if hasattr(progress, 'bar'):
        progress.bar.close()