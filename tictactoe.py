import turtle
from time import sleep

class TicTacToeGame:
    turn = "X"
    game_table = [""] * 9
    wining_combinations = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    t_table = turtle.Turtle()
    t_cross = turtle.Turtle()
    t_zero = turtle.Turtle()
    t_line = turtle.Turtle()
    t_table.hideturtle()
    t_cross.hideturtle()
    t_zero.hideturtle()
    t_line.hideturtle()
    t_table.speed(0)
    t_cross.speed(0)
    t_zero.speed(0)
    t_line.speed(4)
    t_cross.color("red")
    t_zero.color("blue")
    t_line.color("green")
    t_table.width(3)
    t_cross.width(7)
    t_zero.width(7)
    t_line.width(20)


    def __init__(self, size, game_x, game_y):
        self.size = size
        self.game_x = game_x
        self.game_y = game_y
        self.cell = self.size / 3

        self.all_coordinates = {
            "1": (game_x - self.cell, game_y + self.cell),
            "2": (game_x, game_y + self.cell),
            "3": (game_x + self.cell, game_y + self.cell),
            "4": (game_x - self.cell, game_y),
            "5": (game_x, game_y),
            "6": (game_x + self.cell, game_y),
            "7": (game_x - self.cell, game_y - self.cell),
            "8": (game_x, game_y - self.cell),
            "9": (game_x + self.cell, game_y - self.cell)
        }

        self.winning_line_coordinates = {
            1: (game_x - self.cell, game_y + self.cell, game_x + self.cell, game_y + self.cell),
            2: (game_x - self.cell, game_y, game_x + self.cell, game_y),
            3: (game_x - self.cell, game_y - self.cell, game_x + self.cell, game_y - self.cell),
            4: (game_x - self.cell, game_y + self.cell, game_x - self.cell, game_y - self.cell),
            5: (game_x, game_y + self.cell, game_x, game_y - self.cell),
            6: (game_x + self.cell, game_y + self.cell, game_x + self.cell, game_y - self.cell),
            7: (game_x - self.cell, game_y + self.cell, game_x + self.cell, game_y - self.cell),
            8: (game_x + self.cell, game_y + self.cell, game_x - self.cell, game_y - self.cell)
        }

    
    def inv_goto(self, t, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    

    def table(self):
        self.inv_goto(self.t_table, self.game_x - self.size / 2, self.game_y - self.size / 2)

        for i in range(4):
            self.t_table.forward(self.size)
            if i < 3:
                self.t_table.left(90)

        for i in range(2):
            self.inv_goto(self.t_table, self.t_table.xcor() + self.cell, self.game_y + self.size / 2)
            self.t_table.forward(self.size)
        
        self.t_table.left(90)
        for i in range(2):
            self.inv_goto(self.t_table, self.game_x - self.size / 2, self.t_table.ycor() + self.cell)
            self.t_table.forward(self.size)
    

    def cross(self, x, y):
        offset = self.size // 9
        self.inv_goto(self.t_cross, x - offset, y + offset)
        self.t_cross.goto(x + offset, y - offset)
        self.inv_goto(self.t_cross, x + offset, y + offset)
        self.t_cross.goto(x - offset, y - offset)
    

    def zero(self, x, y):
        self.inv_goto(self.t_zero, x, y - self.size // 8)
        self.t_zero.circle(self.size // 8)
    

    def winning_line(self, start_x, start_y, end_x, end_y):
        self.inv_goto(self.t_line, start_x, start_y)
        self.t_line.goto(end_x, end_y)


    def check_table(self):
        count = 1
        for combo in self.wining_combinations:
            if self.game_table[combo[0]] == self.game_table[combo[1]] == self.game_table[combo[2]] and self.game_table[combo[0]] != "":
                return (count, self.game_table[combo[0]])
            count += 1
        
        if "" not in self.game_table:
            return "XO"


    def write_winner(self, winner):
        self.t_line.color("black")
        self.inv_goto(self.t_line, self.game_x, self.game_y - self.cell * 2)
        if winner == "X":
            self.t_line.write("Хрестики виграли!", align="center", font=("Arial", 18, "normal"))
        elif winner == "O":
            self.t_line.write("Нолики виграли!", align="center", font=("Arial", 18, "normal"))
        else:
            self.t_line.write("Ничья!", align="center", font=("Arial", 18, "normal"))
        self.t_line.color("green")


    def restart(self):
        for i in range(3, 0, -1):
            print(f"Рестарт через: {i}")
            sleep(1)

        self.t_cross.clear()
        self.t_zero.clear()
        self.t_line.clear()
        self.game_table = [""] * 9
        self.turn = "X"


    def main_game(self):
        self.table()
        while True:
            user_move = input("Введи номер: ").strip()

            if user_move in self.all_coordinates:
                if self.turn == "X" and not self.game_table[int(user_move) - 1]:
                    self.cross(*self.all_coordinates[user_move])
                    self.game_table[int(user_move) - 1] = "X"
                    self.turn = "O"
                elif self.turn == "O" and not self.game_table[int(user_move) - 1]:
                    self.zero(*self.all_coordinates[user_move])
                    self.game_table[int(user_move) - 1] = "O"
                    self.turn = "X"

                info = self.check_table()

                if info == "XO":
                    self.write_winner(info)
                    self.restart()
                elif info:
                    self.winning_line(*self.winning_line_coordinates[info[0]])
                    self.write_winner(info[1])
                    self.restart()


game = TicTacToeGame(300, 0, 0)
game.main_game()