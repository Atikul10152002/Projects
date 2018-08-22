# /usr/bin/env nim
#[
* The purpose of this program is to create a complicated game of
    Rock, Paper, Scissors, Lizard, Spock.
* The game is made to be played against the Computer.
* The Computer"s input is fully random

The winner is Chosen by the follwing rules:
- Rock blunts Scissors, and Lizard
- Paper covers Rock, disproves Spock
- Scissors cuts Paper, decapitates Lizard
- Lizard poisons Spock, eats Paper
- Spock smashes Scissors, vaporizes Rock
]#


# module that imports random integerd
import strutils
import os
import osproc
import random
randomize()
# import os
# import sys
# import time


# os.system("clear")

echo("\nA GAME MADE BY MOHAMMAD ISLAM\n*The purpose of this program is to create a complicated game of Rock, Paper, Scissors, Lizard, Spock.\n* The game is made to be played against the Computer. \n* The Computer input is fully random \n\n\nThe winner is Chosen by the follwing rules \n- Rock blunts Scissors, and Lizard \n- Paper covers Rock, disproves Spock \n- Scissors cuts Paper, decapitates Lizard \n- Lizard piosons Spock, eats Paper \n- Spock smashes Scissors, vaporizes Rock\n***\nPress \"q\" and \"Enter\" in any point to exit the game...\n___     ___     ___    \n\\  \\    \\  \\    \\  \\   \n \\  \\    \\  \\    \\  \\  \n  )  )    )  )    )  ) \n /  /    /  /    /  /  \n/__/    /__/    /__/")
# time.sleep(1)

# # defination of the whole game

proc GAME() =
    # initial stop set to nothing
    var stop = ""
    while stop != "n":
        # asks the player input
        echo("                     -----\n\n\nRock (r), Paper (p), Scissors (s), Lizard (l), Spock (sp)?  ")
        var 
            player = readline(stdin)
            Computer: string
            Chosen = rand(6)

        # if (player.isalpha()) and (len(player) <= 0):
        if player.len > 0:
            # if player and len(player) <= 1:
            # player inputs
            case toLowerAscii(player)
            of "sp": 
                player = "Spock"
            of "p":
                player= "Paper"
            of "l":
                player = "Lizard"
            of "s":
                player = "Scissors"
            of "r":
                player = "Rock"
            of "q":
                quit()
            of "who":
                echo("me")
            else:
                player = "invalid_input"

            # Computer random choise
            # echoChosen
            # Computer inputs

            if Chosen == 1:
                Computer = "Rock"
            elif Chosen == 2:
                Computer = "Paper"
            elif Chosen == 3:
                Computer = "Scissors"
            elif Chosen == 4:
                Computer = "Lizard"
            else:
                Computer = "Spock"

            echo player, " vs ", Computer
            sleep(1000)

            # easter egg
            if player == "who":
                echo("  _|_|          _|_|_|    _|_|    _|      _|  _|_|_|_|      _|      _|    _|_|    _|_|_|    _|_|_|_|      _|_|_|    _|      _| \n_|    _|      _|        _|    _|  _|_|  _|_|  _|            _|_|  _|_|  _|    _|  _|    _|  _|            _|    _|    _|  _|\n_|_|_|_|      _|  _|_|  _|_|_|_|  _|  _|  _|  _|_|_|        _|  _|  _|  _|_|_|_|  _|    _|  _|_|_|        _|_|_|        _|\n_|    _|      _|    _|  _|    _|  _|      _|  _|            _|      _|  _|    _|  _|    _|  _|            _|    _|      _|\n_|    _|        _|_|_|  _|    _|  _|      _|  _|_|_|_|      _|      _|  _|    _|  _|_|_|    _|_|_|_|      _|_|_|        _|    _|\n                                                                                                                            _|\n\n\n_|      _|    _|_|    _|    _|    _|_|    _|      _|  _|      _|    _|_|    _|_|_|        _|_|_|    _|_|_|  _|          _|_|    _|      _|\n_|_|  _|_|  _|    _|  _|    _|  _|    _|  _|_|  _|_|  _|_|  _|_|  _|    _|  _|    _|        _|    _|        _|        _|    _|  _|_|  _|_|\n_|  _|  _|  _|    _|  _|_|_|_|  _|_|_|_|  _|  _|  _|  _|  _|  _|  _|_|_|_|  _|    _|        _|      _|_|    _|        _|_|_|_|  _|  _|  _|\n_|      _|  _|    _|  _|    _|  _|    _|  _|      _|  _|      _|  _|    _|  _|    _|        _|          _|  _|        _|    _|  _|      _|\n_|      _|    _|_|    _|    _|  _|    _|  _|      _|  _|      _|  _|    _|  _|_|_|        _|_|_|  _|_|_|    _|_|_|_|  _|    _|  _|      _|  ")
            # outcomes
            elif player == Computer:
                echo("It\"s a DRAW!")
            elif player == "Rock" and Computer == "Scissors":
                echo("player wins!")
            elif player == "Rock" and Computer == "Paper":
                echo("Computer wins!")
            elif player == "Rock" and Computer == "Lizard":
                echo("player wins!")
            elif player == "Rock" and Computer == "Spock":
                echo("Computer wins!")

            elif player == "Paper" and Computer == "Rock":
                echo("player wins!")
            elif player == "Paper" and Computer == "Scissors":
                echo("Computer wins!")
            elif player == "Paper" and Computer == "Spock":
                echo("player wins!")
            elif player == "Paper" and Computer == "Lizard":
                echo("Computer wins!")

            elif player == "Scissors" and Computer == "Paper":
                echo("player wins!")
            elif player == "Scissors" and Computer == "Rock":
                echo("Computer wins!")
            elif player == "Scissors" and Computer == "Lizard":
                echo("player wins!")
            elif player == "Scissors" and Computer == "Spock":
                echo("Computer wins!")

            elif player == "Lizard" and Computer == "Paper":
                echo("player wins!")
            elif player == "Lizard" and Computer == "Rock":
                echo("player wins!")
            elif player == "Lizard" and Computer == "Scissors":
                echo("Computer wins!")
            elif player == "Lizard" and Computer == "Spock":
                echo("Computer wins!")

            elif player == "Spock" and Computer == "Paper":
                echo("Computer wins!")
            elif player == "Spock" and Computer == "Rock":
                echo("player wins!")
            elif player == "Spock" and Computer == "Scissors":
                echo("player wins!")
            elif player == "Spock" and Computer == "Lizard":
                echo("Computer wins!")
            else:
                echo("Invalid user input, Computer wins!")
            sleep(1000)
        else:
            echo(
                "\nPlease provide letters only!.\nKey of \"Enter\" and numbers are not considered an option!\n")
#         # stop function
        echo("\n\nDo you want to try again? YES (y) or No (n)?  ")
        stop = readLine(stdin)
        if ("n" in stop) or ("q" in stop) or ("y" in stop):
            if ("n" in stop) or ("q" in stop):
                sleep(1000)
                echo("\nTHANKS FOR TRYING OUT MY GAME...\n")
                sleep(1000)
                quit()
            else:
                echo("...")
        else:
            echo("Sorry your input was counted as no!")
            quit()

GAME()
