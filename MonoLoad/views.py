from flet import *
from pages.home import Home
from pages.download_audio import DOWNLOAD_AUDIO
from pages.download_video import DOWNLOAD_VIDEO

def views_handler(page):

    page.theme_mode = ThemeMode.DARK


    def change_theme_mode(e):

        # Cambia el valode de el page.theme_mode dependiendo del estado en el que se encuentre
        page.theme_mode = ThemeMode.DARK if page.theme_mode != ThemeMode.DARK else ThemeMode.LIGHT

        page.update()        



    # Para ir a la pagina que se desea visitar por medi de los PopupMenuItem
    def change_page(instance: PopupMenuItem, text: str):
        page.go(f'/{text}')


    #Appbar que contiene la navegacion hacia los diferentes apartados de la aplicacion
    appbar = AppBar(title=Text('MonoLoad'), actions=[
        IconButton(icons.WB_SUNNY_OUTLINED, on_click=change_theme_mode),
        PopupMenuButton(
            items=[
                PopupMenuItem(text='Home', on_click=lambda instance: change_page(instance, '')),
                PopupMenuItem(text='Download audio', on_click=lambda instance: change_page(instance, 'download_audio')),
                PopupMenuItem(text='Download video', on_click=lambda instance: change_page(instance, 'download_video'))
            ]
        )
    ] )
    
    

    return {
        '/': View(
            route='/',
            controls=[
                appbar,
                Home(page)
            ]
        ),
        '/download_audio': View(
            route='/download_audio',
            controls=[
                appbar,
                DOWNLOAD_AUDIO(page)
            ]
        ),
        '/download_video': View(
            route='/download_video',
            controls=[
                appbar,
                DOWNLOAD_VIDEO(page)

            ]
        )
    }