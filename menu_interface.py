from tkinter import messagebox

from game import Game


class MenuInterface:
    def __init__(self, window):
        self.window = window
        self.window.create_menu(self.start_game, self.load_game, self.exit_game)

    def start_game(self):
        chosen_difficulty = self.window.get_difficulty()
        game = Game(self.window)
        game.start_game(chosen_difficulty)

    def load_game(self):
        # Logika wczytywania zapisanej gry
        pass

    def exit_game(self):
        if messagebox.askokcancel("Wyjdź z gry", "Czy na pewno chcesz wyjść z gry?"):
            self.window.root.destroy()