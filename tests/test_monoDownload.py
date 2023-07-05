import pytest

from MonoLoad.src.MonoDownloads import audio_download as audio

@pytest.mark.parametrize(
        ("x", "y", "z"),
    [
        ("q","w","e")
    ]
)

def test_if_quality_typed_doesnt_exist(x,y,z):
    assert x == x