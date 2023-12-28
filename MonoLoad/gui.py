from flet import *
from views import views_handler



def main(page: Page) -> None:

    page.title = 'MonoLoad'
    page.window_height = 800
    page.window_width = 1000
    page.window_resizable = True
    

    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
        views_handler(page)[page.route]
        )


    page.on_route_change = route_change
    page.go('/')


    


app(target=main)