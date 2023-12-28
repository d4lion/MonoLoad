from flet import *

class DOWNLOAD_VIDEO(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page


    def build(self):


        return (
            Text('Download Video')
        )