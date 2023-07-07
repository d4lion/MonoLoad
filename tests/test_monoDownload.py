import pytest

from unittest.mock import patch
from os import getcwd, path
from MonoLoad.src.MonoDownloads import audio_download as audio

@pytest.mark.parametrize(
        ("url", "song_name", "quality"),
    [
        ("https://www.youtube.com/watch?v=ARWg160eaX4&pp=ygUJYmFkIGJ1bm51","Neverita", "48kbps"),
        ("https://www.youtube.com/watch?v=ws00k_lIQ9U&pp=ygUJYmFkIGJ1bm51", "Soy Peor", "128kbps"),
        ("https://www.youtube.com/watch?v=CPK_IdHe1Yg&pp=ygUJYmFkIGJ1bm51", "Si Veo a Tu MaMá", "50kbps"),
        ("https://www.youtube.com/watch?v=kLpH1nSLJSs&pp=ygUJYmFkIGJ1bm51", "Amorfoda", "70kbps"),
        ("https://www.youtube.com/watch?v=XA9XGAG6CXM&pp=ygUGbWFsb3J5", "Malory", "160kbps"),
        ("https://www.youtube.com/watch?v=SAvVnVNSvDk&pp=ygUGbWFsb3J5", "Mujeriego", "48kbps")
    ]
)

def test_all_qualities(url, song_name, quality):
    with patch('builtins.input', return_value=quality):
        audio.download(url=url)
    assert path.exists(f"{getcwd()}/downloads/audios/{song_name}.mp3")

