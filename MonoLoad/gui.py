import flet as ft


def main(page: ft.Page):
    global pages

    def change_theme_mode(e):
        if page.theme_mode != ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 700
    page.window_height = 900
    page.window_resizable = False
    page.appbar = ft.AppBar(
        title=ft.Text('MonoLoad'),
        center_title=False,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme_mode),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text='Home', on_click=lambda _: page.go('/')),
                    ft.PopupMenuItem(text='Download Audios', on_click=lambda _: page.go('/download_audios')),
                    ft.PopupMenuItem(text='Download Videos', on_click=lambda _: page.go('/download_videos')),
                ]
            )
        ]
    )

    page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    """
    Se define toda la estrictura para el apartado del home con la ruta (/),
    """

    Home = ft.Row(
        controls=[
            ft.FilledButton(text='Download audios', height=50, on_click=lambda _: page.go('/download_audios')),
            ft.FilledButton(text='Download videos', height=50, on_click=lambda _: page.go('/download_videos')),
        ],
        height=page.window_height - 100,
        width=page.window_width,
        alignment=ft.MainAxisAlignment.CENTER
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
                ft.Text('Download audios')
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
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main)
