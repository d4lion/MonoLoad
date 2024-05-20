import flet as ft
from src.MonoDownloads.audio_dowload_gui import get_audio_resolution, download_audio
from src.transformations import transform_config_to_dict
from time import sleep

# Config
CONFIG: dict = transform_config_to_dict()

# CONSTANTS
WIDTH = CONFIG.get("WIDTH")
HEIGHT = CONFIG.get("HEIGHT")
RESIZABLE = CONFIG.get("WINDOW_RESIZABLE")
MAXIMIZABLE = CONFIG.get("WINDOW_MAXIMIZABLE")
ALWAYS_ON_TOP = CONFIG.get("ALWAYS_ON_TOP")

def main(page: ft.Page):
    global pages

    def change_theme_mode(e):
        if page.theme_mode != ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    # Page Config

    page.title = 'MonoLoad'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = WIDTH
    page.window_height = HEIGHT
    page.window_resizable = RESIZABLE
    page.window_maximizable = MAXIMIZABLE
    page.window_always_on_top = ALWAYS_ON_TOP

    page.appbar = ft.AppBar(
        title=ft.Text('MonoLoad'),
        center_title=False,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,
                          on_click=change_theme_mode),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text='Home', on_click=lambda _: page.go('/')),
                    ft.PopupMenuItem(
                        text='Download Audios', on_click=lambda _: page.go('/download_audios')),
                    ft.PopupMenuItem(
                        text='Download Videos', on_click=lambda _: page.go('/download_videos')),
                ]
            )
        ]
    )

    def route_change(*kwargs):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    """
     __   __  _______  __   __  _______ 
    |  | |  ||       ||  |_|  ||       |
    |  |_|  ||   _   ||       ||    ___|
    |       ||  | |  ||       ||   |___ 
    |       ||  |_|  ||       ||    ___|
    |   _   ||       || ||_|| ||   |___ 
    |__| |__||_______||_|   |_||_______|
    """

    Home = ft.Row(
        controls=[
            ft.FilledButton(text='Download audios', height=50,
                            on_click=lambda _: page.go('/download_audios')),
            ft.FilledButton(text='Download videos', height=50,
                            on_click=lambda _: page.go('/download_videos')),
        ],
        height=page.window_height - 100,
        width=page.window_width,
        alignment=ft.MainAxisAlignment.CENTER
    )

    """
     ______   _______  _     _  __    _  ___      _______  _______  ______  
    |      | |       || | _ | ||  |  | ||   |    |       ||   _   ||      | 
    |  _    ||   _   || || || ||   |_| ||   |    |   _   ||  |_|  ||  _    |
    | | |   ||  | |  ||       ||       ||   |    |  | |  ||       || | |   |
    | |_|   ||  |_|  ||       ||  _    ||   |___ |  |_|  ||       || |_|   |
    |       ||       ||   _   || | |   ||       ||       ||   _   ||       |
    |______| |_______||__| |__||_|  |__||_______||_______||__| |__||______|                                                                                                                                                                                       
    """

    qualities = ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                       spacing=40, scroll=ft.ScrollMode.AUTO)
    NameTextField = ft.TextField(label='Name')
    UrlTextField = ft.TextField(label='Url')

    def get_resolutions(e):
        global video
        url = UrlTextField.value
        qualities.clean()

        def close_banner(e):
            page.banner.open = False
            page.update()

        try:
            resolutions, video = get_audio_resolution(url)

            for resolution in resolutions:
                qualities.controls.append(ft.Checkbox(label=resolution))

            qualities.update()
        except Exception as e:
            page.banner = ft.Banner(
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED,
                                color=ft.colors.AMBER, size=40),
                content=ft.Text(
                    "It seems that you have used an incorrect or invalid url, please check it and try again."
                ),
                actions=[
                    ft.TextButton("Retry", on_click=close_banner)
                ]
            )

            page.banner.open = True
            page.update()

    def download_mono_audios(e):
        dic = {}
        for checkBox in qualities.controls:
            dic[checkBox.label] = checkBox.value

        for key, value in dic.items():
            if value:
                    # Se realiza el llamado al snack_bar para decirle al usuario donde se guarda su archivo
                out_path = download_audio(
                    video, key, video_title=NameTextField.value)
                page.snack_bar = ft.SnackBar(ft.Text(out_path))
                page.snack_bar.open = True
                sleep(0.2)
                page.update()

    DownloadAudios = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text('MonoLoad', text_align=ft.alignment.center),
                NameTextField,
                UrlTextField,
                qualities,
                ft.Row(
                    controls=[
                        ft.FilledButton(text='Resolution',
                                        height=50, on_click=get_resolutions),
                        ft.FilledButton(text='Download', height=50,
                                        on_click=download_mono_audios)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40
                )
            ],
            height=page.window_height - 300,
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=page.window_width,
        alignment=ft.alignment.center,
        margin=10,
        padding=10
    )

    pages = {
        '/': ft.View(
            '/', [
                page.appbar,
                Home
            ]
        ),
        '/download_audios': ft.View(
            '/download_audios', [
                page.appbar,
                DownloadAudios
            ]
        ),
        '/download_videos': ft.View(
            '/download_videos', [
                page.appbar,
                ft.Text('Download videos')
            ]
        )
    }

    page.on_route_change = route_change
    page.go('/')
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
