import flet as ft
from src.transformations import transform_config_to_dict
from src.Routes import Router

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

    def RouteChange(*kwargs):

        routes = Router.pages(page)

        page.views.clear()
        page.views.append(
            routes[page.route]
        )

    page.on_route_change = RouteChange
    page.go('/')
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
