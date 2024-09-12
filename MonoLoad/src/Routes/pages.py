import flet as ft


def HomeComponent(page):
    """
    Creates the home component with two buttons to download audios and videos
    Args:
        page (ft.Page): The page object
    Returns:
        Component (ft.Row) with two buttons
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

    return Home


def DowloadAudioComponent(page):
    from time import sleep
    from MonoLoad.src.MonoDownloads.audio_dowload_gui import get_audio_resolution, download_audio

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
            print(e)
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

    return DownloadAudios
