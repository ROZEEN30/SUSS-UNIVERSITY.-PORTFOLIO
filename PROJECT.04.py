import random
from tkinter import *

WIDTH = 800
HEIGHT = 500
GRID_SIZE = 50
INITIAL_LENGTH = 3
GAME_SPEED = 300
FOOD_COLOR = "#FF0000"
SNAKE_COLOR = "#0000FF"
BACKGROUND_COLOR = "#000000"

root = Tk()
root.title("Classic Snake Game")
root.resizable(False, False)

score = 0
movement = "down"

score_label = Label(root, text=f"Score: {score}", font=("consolas", 30), fg="white", bg="black")
score_label.pack()

game_canvas = Canvas(root, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
game_canvas.pack()

root.update()

win_width = root.winfo_width()
win_height = root.winfo_height()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
pos_x = int((screen_w / 2) - (win_width / 2))
pos_y = int((screen_h / 2) - (win_height / 2))
root.geometry(f"{win_width}x{win_height}+{pos_x}+{pos_y}")

class PlayerSnake:
    def __init__(self):
        self.size = INITIAL_LENGTH
        self.body = []
        self.blocks = []

        for i in range(self.size):
            self.body.append([250, 250 - i * GRID_SIZE])

        for x, y in self.body:
            part = game_canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.blocks.append(part)

class GameFood:
    def __init__(self):
        self.position = self.spawn_food()
        self.food_item = game_canvas.create_oval(
            self.position[0], self.position[1],
            self.position[0] + GRID_SIZE, self.position[1] + GRID_SIZE,
            fill=FOOD_COLOR, tags="food"
        )

    def spawn_food(self):
        while True:
            x_food = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
            y_food = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
            if [x_food, y_food] not in snake.body:
                return [x_food, y_food]

# Game Logic
def update_game(snake, food):
    global movement, score

    x_snake, y_snake = snake.body[0]

    if movement == "up":
        y_snake -= GRID_SIZE
    elif movement == "down":
        y_snake += GRID_SIZE
    elif movement == "left":
        x_snake -= GRID_SIZE
    elif movement == "right":
        x_snake += GRID_SIZE

    snake.body.insert(0, [x_snake, y_snake])
    new_block = game_canvas.create_rectangle(x_snake, y_snake, x_snake + GRID_SIZE, y_snake + GRID_SIZE, fill=SNAKE_COLOR, tags="snake")
    snake.blocks.insert(0, new_block)

    if [x_snake, y_snake] == food.position:
        score += 1
        score_label.config(text=f"Score: {score}")
        game_canvas.delete(food.food_item)
        food = GameFood()  # Generate new food
    else:
        del snake.body[-1]
        game_canvas.delete(snake.blocks[-1])
        del snake.blocks[-1]

    if detect_collision(snake):
        end_game()
        return

    root.after(GAME_SPEED, update_game, snake, food)


def set_direction(new_movement):
    global movement
    if new_movement == "left" and movement != "right":
        movement = "left"
    elif new_movement == "right" and movement != "left":
        movement = "right"
    elif new_movement == "up" and movement != "down":
        movement = "up"
    elif new_movement == "down" and movement != "up":
        movement = "down"

def detect_collision(snake):
    head_x, head_y = snake.body[0]

    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        return True

    for segment in snake.body[1:]:
        if head_x == segment[0] and head_y == segment[1]:
            return True
    return False

def end_game():
    game_canvas.delete("all")
    game_canvas.create_text(WIDTH / 2, HEIGHT / 2, font=("consolas", 50, "bold"), text="GAME OVER!", fill="red", tags="game_over")

root.bind("<Left>", lambda event: set_direction("left"))
root.bind("<Right>", lambda event: set_direction("right"))
root.bind("<Up>", lambda event: set_direction("up"))
root.bind("<Down>", lambda event: set_direction("down"))

snake = PlayerSnake()
food = GameFood()
update_game(snake, food)

root.mainloop()
