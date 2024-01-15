from cell_states import HiddenState


class Cell:
    def __init__(self, x, y):
        self.state = HiddenState(self)
        self.is_mine = False
        self.neighbor_mines = 0
        self.x = x
        self.y = y

    def reveal(self, game):
        self.state.reveal(game)

    def reveal_bomb(self):
        self.state.reveal_bomb()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def mark(self):
        self.state.mark()

    def set_state(self, state):
        self.state = state

    def toggle_mine(self):
        self.is_mine = not self.is_mine

    def set_neighbor_mines(self, count):
        self.neighbor_mines = count

    def __repr__(self):
        return self.state.__repr__()