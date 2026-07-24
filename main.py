# -*- coding: utf-8 -*-

from Tkinter import *
import random

def game_win(user, computer):

    if user == computer:
        return None

    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False

    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False

    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False


def play(user):

    choices = {
        "s": "Snake",
        "w": "Water",
        "g": "Gun"
    }

    computer = random.choice(["s", "w", "g"])

    result = game_win(user, computer)

    if result is None:
        winner = "MATCH DRAW"
    elif result:
        winner = "YOU WIN!"
    else:
        winner = "COMPUTER WINS!"

    result_label.config(
        text="Your Choice : {}\nComputer : {}\n\n{}".format(
            choices[user],
            choices[computer],
            winner
        )
    )


root = Tk()
root.title("Snake Water Gun Game")
root.geometry("400x400")
root.resizable(False, False)

Label(root,
      text="Snake Water Gun Game",
      font=("Arial", 18, "bold")).pack(pady=15)

Label(root,
      text="Choose Your Weapon",
      font=("Arial", 12)).pack()

Button(root,
       text="Snake",
       width=15,
       height=2,
       command=lambda: play("s")).pack(pady=5)

Button(root,
       text="Water",
       width=15,
       height=2,
       command=lambda: play("w")).pack(pady=5)

Button(root,
       text="Gun",
       width=15,
       height=2,
       command=lambda: play("g")).pack(pady=5)

result_label = Label(root,
                     text="",
                     font=("Arial", 12),
                     fg="blue")

result_label.pack(pady=20)

root.mainloop()