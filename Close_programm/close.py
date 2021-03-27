
from menu import Menu

class Close(Menu):

    def close(self):
        close = Menu.menu(self)
        while True:
            if close == 3:
                return Menu.menu(self)


