import pytest
import unittest

from pytest import MonkeyPatch
from unittest.mock import patch
from os import getcwd, listdir, path
from MonoLoad.src.MonoDownloads import audio_download as audio

@pytest.mark.parametrize(
        ("url", "song_name"),
    [
        ("https://www.youtube.com/watch?v=ARWg160eaX4&pp=ygUJYmFkIGJ1bm51","Neverita"),
        ("https://www.youtube.com/watch?v=ws00k_lIQ9U&pp=ygUJYmFkIGJ1bm51", "Soy Peor"),
        ("https://www.youtube.com/watch?v=CPK_IdHe1Yg&pp=ygUJYmFkIGJ1bm51", "Si Veo a Tu MaMá"),
        ("https://www.youtube.com/watch?v=kLpH1nSLJSs&pp=ygUJYmFkIGJ1bm51", "Amorfoda"),
        ("https://www.youtube.com/watch?v=XA9XGAG6CXM&pp=ygUGbWFsb3J5", "Malory"),
        ("https://www.youtube.com/watch?v=SAvVnVNSvDk&pp=ygUGbWFsb3J5", "Mujeriego")
    ]
)

def test_if_quality_typed_doesnt_exist(url, song_name):
    with patch('builtins.input', return_value='1kbps'):
        audio.download(url=url)
    assert path.exists(f"{getcwd()}/downloads/audios/{song_name}.mp3")

def test_download_and_save(url, song_name):
    pass