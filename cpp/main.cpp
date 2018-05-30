#include <iostream>
#include <string>
#include <map>
#include <ctime>
#include <cstdlib>
#include <cctype>
using namespace std;

void game();

int main ()
{
  /*
  * The purpose of this program is to create a complicated game of
      Rock, Paper, Scissors, Lizard, Spock.
  * The game is made to be played against the COMPUTER.
  * The COMPUTER's input is fully random

  The winner is CHOSEN by the follwing rules:
  - Rock blunts Scissors, and Lizard
  - Paper covers Rock, disproves Spock
  - Scissors cuts Paper, decapitates Lizard
  - Lizard poisons Spock, eats Paper
  - Spock smashes Scissors, vaporizes Rock

  # module that imports random integerd
  from random import randint
  import os
  import sys
  import time
  */
  srand(time(0));

  cout << "\n A GAME MADE BY MOHAMMAD ISLAM\n *The purpose of this program is to \
  create a complicated game of Rock, Paper, Scissors, Lizard, Spock.\n * \
  The game is made to be played against the COMPUTER. \n* The COMPUTER input is \
  fully random \n\n\nThe winner is CHOSEN by the follwing rules \n- Rock blunts \
  Scissors, and Lizard \n- Paper covers Rock, disproves Spock \n- Scissors cuts \
  Paper, decapitates Lizard \n- Lizard piosons Spock, eats Paper \n- Spock smashes \
  Scissors, vaporizes Rock\n***\nPress \'q\' and \'Enter\' in any point to exit the game...\
  \n ___     ___     ___    \
  \n \\  \\    \\  \\    \\  \\   \
  \n  \\  \\    \\  \\    \\  \\  \
  \n   )  )    )  )    )  ) \
  \n  /  /    /  /    /  /  \
  \n /__/    /__/    /__/ ";

  game();

}


// defination of the whole game
void game()
{
  // initial stop set to nothing
  string stop = "n";
  cout << stop;
  string PLAYER;
    while (stop == "n"){
      // asks the player input
      cout << "\n\n\nWhat do you want to play? \n[r]ock, [p]aper, [s]cissors, [l]izard, [sp]ock? >> ";
      cin >> PLAYER;
      
      if (PLAYER == "sp"){
          PLAYER = "Spock";
      }
      else if (PLAYER == "p"){
        PLAYER = "Paper";
      }
      else if (PLAYER == "l"){
        PLAYER = "Lizard";
      }
      else if (PLAYER == "s"){
        PLAYER = "Scissors";
      }
      else if (PLAYER == "r"){
        PLAYER = "Rock";
      }
      else if (PLAYER == "q"){
        break;
      }
      else if(PLAYER == "who"){
        cout << "me" << endl;
      }
      else{
        PLAYER = "invalid_input";
      }
      cout << PLAYER << endl;
      stop = "y";
    }
              // 
//             # computer random choise
//             CHOSEN = randint(1, 5)
//             # print CHOSEN
//             # computer inputs
//             if CHOSEN == 1:
//                 COMPUTER = "Rock"
//             elif CHOSEN == 2:
//                 COMPUTER = "Paper"
//             elif CHOSEN == 3:
//                 COMPUTER = "Scissors"
//             elif CHOSEN == 4:
//                 COMPUTER = "Lizard"
//             else:
//                 COMPUTER = "Spock"
//             print (PLAYER, "vs", COMPUTER)
//             time.sleep(1)
//             # easter egg
//             if PLAYER == "who":
//                 print ("  _|_|          _|_|_|    _|_|    _|      _|  _|_|_|_|      _|      _|    _|_|    _|_|_|    _|_|_|_|      _|_|_|    _|      _| \n_|    _|      _|        _|    _|  _|_|  _|_|  _|            _|_|  _|_|  _|    _|  _|    _|  _|            _|    _|    _|  _|\n_|_|_|_|      _|  _|_|  _|_|_|_|  _|  _|  _|  _|_|_|        _|  _|  _|  _|_|_|_|  _|    _|  _|_|_|        _|_|_|        _|\n_|    _|      _|    _|  _|    _|  _|      _|  _|            _|      _|  _|    _|  _|    _|  _|            _|    _|      _|\n_|    _|        _|_|_|  _|    _|  _|      _|  _|_|_|_|      _|      _|  _|    _|  _|_|_|    _|_|_|_|      _|_|_|        _|    _|\n                                                                                                                            _|\n\n\n_|      _|    _|_|    _|    _|    _|_|    _|      _|  _|      _|    _|_|    _|_|_|        _|_|_|    _|_|_|  _|          _|_|    _|      _|\n_|_|  _|_|  _|    _|  _|    _|  _|    _|  _|_|  _|_|  _|_|  _|_|  _|    _|  _|    _|        _|    _|        _|        _|    _|  _|_|  _|_|\n_|  _|  _|  _|    _|  _|_|_|_|  _|_|_|_|  _|  _|  _|  _|  _|  _|  _|_|_|_|  _|    _|        _|      _|_|    _|        _|_|_|_|  _|  _|  _|\n_|      _|  _|    _|  _|    _|  _|    _|  _|      _|  _|      _|  _|    _|  _|    _|        _|          _|  _|        _|    _|  _|      _|\n_|      _|    _|_|    _|    _|  _|    _|  _|      _|  _|      _|  _|    _|  _|_|_|        _|_|_|  _|_|_|    _|_|_|_|  _|    _|  _|      _|  ")
//             # outcomes
//             elif PLAYER == COMPUTER:
//                 print ("It\"s a DRAW!")
//             elif PLAYER == "Rock" and COMPUTER == "Scissors":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Rock" and COMPUTER == "Paper":
//                 print (str("COMPUTER wins!").upper())
//             elif PLAYER == "Rock" and COMPUTER == "Lizard":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Rock" and COMPUTER == "Spock":
//                 print (str("COMPUTER wins!").upper())

//             elif PLAYER == "Paper" and COMPUTER == "Rock":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Paper" and COMPUTER == "Scissors":
//                 print (str("COMPUTER wins!").upper())
//             elif PLAYER == "Paper" and COMPUTER == "Spock":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Paper" and COMPUTER == "Lizard":
//                 print (str("COMPUTER wins!").upper())

//             elif PLAYER == "Scissors" and COMPUTER == "Paper":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Scissors" and COMPUTER == "Rock":
//                 print (str("COMPUTER wins!").upper())
//             elif PLAYER == "Scissors" and COMPUTER == "Lizard":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Scissors" and COMPUTER == "Spock":
//                 print (str("COMPUTER wins!").upper())

//             elif PLAYER == "Lizard" and COMPUTER == "Paper":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Lizard" and COMPUTER == "Rock":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Lizard" and COMPUTER == "Scissors":
//                 print (str("COMPUTER wins!").upper())
//             elif PLAYER == "Lizard" and COMPUTER == "Spock":
//                 print (str("COMPUTER wins!").upper())

//             elif PLAYER == "Spock" and COMPUTER == "Paper":
//                 print (str("COMPUTER wins!").upper())
//             elif PLAYER == "Spock" and COMPUTER == "Rock":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Spock" and COMPUTER == "Scissors":
//                 print (str("PLAYER wins!").upper())
//             elif PLAYER == "Spock" and COMPUTER == "Lizard":
//                 print (str("COMPUTER wins!").upper())
//             else:
//                 print ("Invalid user input, COMPUTER wins!")
//             time.sleep(1)

//         stop = input(
//             "\n\nDo you want to try again? YES (y) or No (n)?  ")
//         if ("n" in stop.lower()) or ("q" in stop.lower()) or ("y" in stop.lower()):
//             if ("n" in stop.lower()) or ("q" in stop.lower()):
//                 time.sleep(1)
//                 print ('\nTHANKS FOR TRYING OUT MY GAME...\n')
//                 time.sleep(1)
//                 sys.exit()
//             else:
//                 os.system('clear')
//                 print ("...")
//         else:
//             print ("Sorry your input was counted as no!")
//             sys.exit()
}