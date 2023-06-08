from pytube import YouTube, streams
from colorama import init, Fore
from .itags import audio_itags_quality

init(autoreset=True)

def download(url, out_path="downloads/audios"):

    def get_resolution(streams_data):
        resolutions = list()

        for stream in streams_data:
            resolutions.append(stream.abr)

        return resolutions
    
    def audio_quality_dowload(resolutions, video):
        print(f"\n video title: {Fore.RED + video.title} \n {Fore.WHITE} \n qualities: {resolutions}")

        audio_quality_dowload = input("\n Type the quality: ")
        
        return audio_quality_dowload
        


    try:
        video = YouTube(url)
        streams_data = video.streams.filter(only_audio=True)
        resolutions = get_resolution(streams_data=streams_data)

        audio_qulity_to_dowload = audio_quality_dowload(resolutions=resolutions, video=video)

        stream = video.streams.get_by_itag(audio_itags_quality.get(audio_qulity_to_dowload))
        stream.download(output_path=out_path)
        print(f"\n {Fore.GREEN} Done!!")
    except Exception as e:
        print(f"\n {e} \n Check the video url and try again.")
