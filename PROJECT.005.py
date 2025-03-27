import tkinter

def set_title(row, column):
    global current_player
    if board[row][column]["text"] != "":
        return
    board[row][column]["text"] = current_player
    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1
    label["text"] = current_player + "'s turn"

    check_winner()

def check_winner():
    global turn, game_over
    turn += 1

    # Check rows
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != "":
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_lightgrey)
            game_over = True
            return

    # Check columns
    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != "":
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_lightgrey)
            game_over = True
            return

    # Check diagonals
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "":
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_lightgrey)
        game_over = True
        return

    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "":
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_lightgrey)
        board[1][1].config(foreground=color_yellow, background=color_lightgrey)
        board[2][0].config(foreground=color_yellow, background=color_lightgrey)
        game_over = True
        return

    # Check for tie
    if turn == 9 and not game_over:
        game_over = True
        label.config(text="It's a Tie!", foreground=color_yellow)

def new_game():
    global turn, game_over, current_player
    turn = 0
    game_over = False
    current_player = player_1
    label.config(text=player_1 + "'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=background_color)

# Game Settings
player_1 = "X"
player_2 = "O"
current_player = player_1

color_blue = "#FF0000"
color_yellow = "#0000FF"
background_color = "#000000"
color_lightgrey = "#D3D3D3"
color_grey = "#00FF00"

# Initialize Window
window = tkinter.Tk()
window.title("TIC TAC TOE")
window.resizable(False, False)

turn = 0
game_over = False

# Create Frame
frame = tkinter.Frame(window)
frame.pack()

# Create Label
label = tkinter.Label(frame, text=player_1 + "'s turn", font=("Consolas", 20), background=background_color, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# Create Board
board = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(
            frame,
            text="",
            font=("Consolas", 50, "bold"),
            background=background_color,
            foreground=color_blue,
            width=4,
            height=1,
            command=lambda r=row, c=column: set_title(r, c)
        )
        board[row][column].grid(row=row + 1, column=column)

# Create Restart Button
button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=color_grey, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

# Center Window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Run the Game
window.mainloop()
