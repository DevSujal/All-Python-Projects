import random

str = ["stone", "paper", "scissor"]
rematch = "yes"
while rematch == "yes":
    computersChoice = str[random.randint(0, 2)]
    usersChoice = input("enter stone paper or scissor : ")

    if computersChoice == usersChoice:
        print(
            f"Match is drawn\nyour choice = {usersChoice}\nrandom choice = {computersChoice}"
        )
    elif (
        (computersChoice == "scissor" and usersChoice == "paper")
        or (computersChoice == "stone" and usersChoice == "scissor")
        or (computersChoice == "paper" and usersChoice == "stone")
    ):
        print(
            f"sorry you loose the match\nyour choice = {usersChoice}\nrandom choice = {computersChoice}"
        )
    else:
        print(
            f"congratulations you win the match\nyour choice = {usersChoice}\nrandom choice = {computersChoice}"
        )
    rematch = input("would you like to play again please enter yes or no : ")
