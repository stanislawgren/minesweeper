class CellState:
    def __init__(self, cell):
        self.cell = cell

    def reveal(self, game):
        pass

    def reveal_bomb(self):
        pass

    def mark(self):
        pass

class HiddenState(CellState):
    def reveal(self, game):
        if self.cell.is_mine:
            self.reveal_bomb()
            game.lost_game()
        else:
            self.cell.set_state(RevealedState(self.cell))

    def reveal_bomb(self):
        self.cell.set_state(RevealedBombState(self.cell))

    def mark(self):
        self.cell.set_state(MarkedState(self.cell))

    def __repr__(self):
        return "hidden"

class RevealedState(CellState):
    def reveal(self, game):
        # Nic nie rób, komórka jest już odsłonięta
        pass

    def __repr__(self):
        return f"{self.cell.neighbor_mines}" if self.cell.neighbor_mines > 0 else "revealed"

class MarkedState(CellState):
    def reveal(self, game):
        if self.cell.is_mine:
            self.reveal_bomb()
            game.lost_game()

    def reveal_bomb(self):
        self.cell.set_state(RevealedBombState(self.cell))

    def mark(self):
        self.cell.set_state(HiddenState(self.cell))

    def __repr__(self):
        return "marked"

class RevealedBombState(CellState):
    def reveal(self, game):
        pass

    def __repr__(self):
        return "💣"