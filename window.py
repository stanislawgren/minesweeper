import tkinter as tk
from tkinter import messagebox

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Saper")
        self.root.configure(bg='black')

        self.menu_frame = tk.Frame(self.root, bg='black')
        self.menu_frame.pack()
        self.board_frame = None
        self.difficulty = tk.StringVar(value="łatwy")
        self.board_cells = []
        self.timer_id = None  # Variable to store the timer ID
        self.timer_value = None

    def create_menu(self, start_game_callback, load_game_callback, exit_game_callback):
        button_style = {'bg': 'white', 'fg': 'black'}

        difficulty_frame = tk.LabelFrame(self.menu_frame, text="Poziom trudności", padx=10, pady=10, bg='black', fg='white')
        difficulty_frame.pack(padx=10, pady=10)

        easy_radio = tk.Radiobutton(difficulty_frame, text="Łatwy", variable=self.difficulty, value="łatwy", bg='black', fg='white')
        easy_radio.pack(anchor=tk.W)

        medium_radio = tk.Radiobutton(difficulty_frame, text="Średni", variable=self.difficulty, value="średni", bg='black', fg='white')
        medium_radio.pack(anchor=tk.W)

        hard_radio = tk.Radiobutton(difficulty_frame, text="Trudny", variable=self.difficulty, value="trudny", bg='black', fg='white')
        hard_radio.pack(anchor=tk.W)

        start_button = tk.Button(self.menu_frame, text="Zacznij grę", command=start_game_callback, **button_style)
        start_button.pack(pady=10)

        load_button = tk.Button(self.menu_frame, text="Załaduj grę", command=load_game_callback, **button_style)
        load_button.pack(pady=10)

        exit_button = tk.Button(self.menu_frame, text="Wyjdź z gry", command=exit_game_callback, **button_style)
        exit_button.pack(pady=10)

    def display_board(self, board, game):
        self.menu_frame.pack_forget()

        # Ramka na górną część interfejsu (score i timer)
        top_frame = tk.Frame(self.root, bg='black')
        top_frame.pack(side=tk.TOP, fill=tk.X)

        # Pole SCORE
        self.marks_label = tk.Label(top_frame, text="MARKS LEFT: 0", bg='black', fg='white')
        self.marks_label.pack(side=tk.LEFT, padx=10)

        # Pole TIMER
        self.timer_label = tk.Label(top_frame, text="TIMER: 0", bg='black', fg='white')
        self.timer_label.pack(side=tk.RIGHT, padx=10)

        self.start_timer()

        self.board_frame = tk.Frame(self.root, bg='black')
        self.board_frame.pack()

        for index, row in enumerate(board.cells):
            self.board_cells.append([])
            row_frame = tk.Frame(self.board_frame, bg='black')
            row_frame.pack(side=tk.TOP)
            for cell in row:
                cell_frame = tk.Frame(row_frame, width=35, height=35, bg='grey', highlightbackground='black', highlightthickness=3)
                cell_frame.pack(side=tk.LEFT, padx=2, pady=2)
                cell_frame.bind('<Button-1>', game.cell_click)
                cell_frame.bind('<Button-3>', game.cell_click)
                cell_frame.cell = cell
                self.board_cells[index].append(cell_frame)

    def update_marks(self, score):
        self.marks_label.config(text=f"MARKS LEFT: {score}")

    def update_timer(self):
        current_time = int(self.timer_label.cget("text").split(": ")[1])
        self.timer_value = current_time + 1
        self.timer_label.config(text=f"TIMER: {current_time + 1}")
        self.timer_id = self.root.after(1000, self.update_timer)

    def start_timer(self):
        self.timer_label.config(text="TIMER: 0")
        self.update_timer()

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def get_difficulty(self):
        return self.difficulty.get()

    def show_popup(self, title, message):
        popup = tk.Tk()
        popup.title(title)

        label = tk.Label(popup, text=message)
        label.pack(padx=10, pady=10)

        # Function to be called when closing the popup
        def on_close():
            popup.destroy()
            self.root.destroy()  # Close the main program window

        close_button = tk.Button(popup, text="Close", command=on_close)
        close_button.pack(pady=10)

        popup.protocol("WM_DELETE_WINDOW", on_close)  # Handle window close event

        popup.mainloop()

    def run(self):
        self.root.mainloop()
