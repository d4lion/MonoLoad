from MonoLoad.src.Routes.pages import HomeComponent, DowloadAudioComponent
import flet as ft


def pages(page):
    _pages = {
        '/': ft.View(
            '/', [
                page.appbar,
                HomeComponent(page)
            ]
        ),
        '/download_audios': ft.View(
            '/download_audios', [
                page.appbar,
                DowloadAudioComponent(page)
            ]
        ),
        '/download_videos': ft.View(
            '/download_videos', [
                page.appbar,
                ft.Text('Download videos')
            ]
        )
    }

    return _pages
