from board import Board
import tkinter as tk
import random

class Game:
    def __init__(self, window):
        self.window = window
        self.board = None
        self.first_click = True
        self.bombs = None
        self.marked = []
        self.marks_left = None

    def start_game(self, difficulty):
        if difficulty == "łatwy":
            size = 10
            self.bombs = 10
            self.marks_left = 10
        elif difficulty == "średni":
            size = 20
            self.bombs = 20
            self.marks_left = 20
        elif difficulty == "trudny":
            size = 30
            self.bombs = 30
            self.marks_left = 30
        else:
            raise ValueError("Nieznany poziom trudności")

        self.board = Board(size, size)
        self.window.display_board(self.board, self)
        self.window.update_marks(self.marks_left)

    def cell_click(self, event):
        click_range = 2
        cell_frame = event.widget
        cell = cell_frame.cell

        if self.first_click:
            self.board.generate_board(self.bombs, cell.get_x(), cell.get_y())
            self.first_click = False
            if self.bombs == 10: click_range = 50
            if self.bombs == 20: click_range = 200
            if self.bombs == 30: click_range = 500

        if event.num == 1:  # Lewy przycisk myszy
            if not cell.is_mine and cell.neighbor_mines == 0:
                self.reveal_empty_cells(cell.get_x(), cell.get_y(), click_range)
            cell.reveal(self)
        elif event.num == 3:  # Prawy przycisk myszy
            if self.marks_left > 0:
                if str(cell) == "hidden":
                    self.marked.append([cell.get_x(), cell.get_y()])
                    self.marks_left -= 1
                if str(cell) == "marked":
                    self.marked.pop(self.marked.index([cell.get_x(), cell.get_y()]))
                    self.marks_left += 1
                cell.mark()
            else:
                if str(cell) == "marked":
                    self.marked.pop(self.marked.index([cell.get_x(), cell.get_y()]))
                    self.marks_left += 1
                    cell.mark()

        self.window.update_marks(self.marks_left)

        has_won = self.check_win_condition()

        if has_won:
            self.game_won()

        self.update_cell_display(cell_frame, cell)

    import random

    def reveal_empty_cells(self, x, y, click_range):
        queue = [(y, x)]
        visited = set()
        target_neighbor_mines = self.bombs + click_range

        while queue:
            current_x, current_y = queue.pop(0)
            current_cell_frame = self.window.board_cells[current_x][current_y]
            current_cell = current_cell_frame.cell

            if str(current_cell) == "hidden" and not current_cell.is_mine and current_cell.neighbor_mines <= 3:
                current_cell.reveal(self)
                self.update_cell_display(current_cell_frame, current_cell)

                target_neighbor_mines -= 1
                if target_neighbor_mines == 0:
                    return

                if not current_cell.is_mine:
                    neighbors = [(ni, nj) for ni in range(max(0, current_x - 1), min(self.board.width, current_x + 2))
                                 for nj in range(max(0, current_y - 1), min(self.board.width, current_y + 2))]
                    

                    for ni, nj in neighbors:
                        if (ni, nj) not in visited:
                            queue.append((ni, nj))
                            visited.add((ni, nj))

    def check_win_condition(self):
        if self.marks_left == 0:
            bombs_found = 0
            bombs_arr = self.board.get_bombs_arr()
            for mark in self.marked:
                if mark in bombs_arr:
                    bombs_found+=1

            if bombs_found == self.bombs:
                return True
            else:
                return False
        else:
            return False

    def lost_game(self):
        self.window.stop_timer()
        for row in self.window.board_cells:
            for cell in row:
                xcell = cell.cell
                if xcell.is_mine:
                    xcell.reveal_bomb()
                    self.update_cell_display(cell, xcell)

        self.window.show_popup("przegrales gre", "no wybuchles co nie")

    def game_won(self):
        self.window.stop_timer()
        for row in self.window.board_cells:
            for cell in row:
                xcell = cell.cell
                if xcell.is_mine:
                    xcell.reveal_bomb()
                    self.update_cell_display(cell, xcell)

        self.window.show_popup("wygrales gre", f"Gratuluje! Ukonczyłeś gre z wynikiem: {self.window.timer_value} sekund!")

    def update_cell_display(self, cell_frame, cell):

        cell_frame.config(width=35, height=35)

        if cell.state.__repr__() == "hidden":
            cell_frame.config(bg='grey')
        elif cell.state.__repr__() == "marked":
            cell_frame.config(bg='red')
        elif cell.state.__repr__() == "💣":
            cell_frame.config(bg='red')
            text = str(cell)
            label = tk.Label(cell_frame, text=text, bg='red', anchor="center")
            label.place(relx=0.5, rely=0.5, anchor="center")
        else:
            cell_frame.config(bg='white')
            if str(cell) == "revealed":
                text = ""
            else:
                text = str(cell)
            label = tk.Label(cell_frame, text=text, bg='white', anchor="center")
            label.place(relx=0.5, rely=0.5, anchor="center")

    def save_game(self):
        # Zapis stanu gry
        pass

    def load_game(self):
        # Wczytanie zapisanej gry
        pass
