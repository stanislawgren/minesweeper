from menu_interface import MenuInterface
from window import Window

if __name__ == "__main__":
    window = Window()
    menu_interface = MenuInterface(window)
    window.run()