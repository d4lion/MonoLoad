from flet import *

class Home(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
 
    

    def build(self):


        def hello(e):
            print('Hello')
                    
        return(
            
            Column(
                controls=[
              Text('Welcome to the homepage'),
              TextButton(text='Hello', on_click=hello)
              
                ]
              
            )
        )

              
    