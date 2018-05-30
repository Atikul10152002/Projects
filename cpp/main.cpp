#include <iostream>
#include <string>
#include <ctime>
import std;

using namespace std;


void game();
string playerIfelse(string);
string computerIfelse(int);
string outcomeIfelse(string, string);


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

  # py modules 
  from random import randint
  import os
  import sys
  import time
  */

  cout << "\n A GAME MADE BY MOHAMMAD ISLAM\n* The purpose of this program is to\
  create a complicated game of Rock, Paper, Scissors, Lizard, Spock.\n* The\
  game is made to be played against the COMPUTER. \n* The COMPUTER input is\
  fully random \n\n\nThe winner is CHOSEN by the follwing rules \n- Rock blunts\
  Scissors, and Lizard \n- Paper covers Rock, disproves Spock \n- Scissors cuts\
  Paper, decapitates Lizard \n- Lizard piosons Spock, eats Paper \n- Spock smashes\
  Scissors, vaporizes Rock\n***\nPress \'q\' and \'Enter\' in any point to exit the game...\
  \n ___     ___     ___    \
  \n \\  \\    \\  \\    \\  \\   \
  \n  \\  \\    \\  \\    \\  \\  \
  \n   )  )    )  )    )  ) \
  \n  /  /    /  /    /  /  \
  \n /__/    /__/    /__/ " << endl;

  game();

}


// defination of the whole game
static string stop = "n";

void game()
{
  srand(time(0));
  // initial stop set to nothing
  string p_choice;
  
    while (stop == "n"){
      // stop = "y";
      // asks the player input
      cout << "\n\nWhat do you want to play? \n[r]ock, [p]aper, [s]cissors, [l]izard, [sp]ock? >> ";
      cin >> p_choice;
      
      if (p_choice != "q"){
        string PLAYER = playerIfelse(p_choice);
      
        // computer random choise
        string COMPUTER = computerIfelse(rand()%5);
        
        // Result
        cout << "PLAYER" << " vs. " << "COMPUTER" << endl;
        cout << PLAYER << " vs. " << COMPUTER << endl;
      
        // Outcomes
        string OUTCOME = outcomeIfelse(PLAYER, COMPUTER);
        cout << OUTCOME<< endl;

        //Again 
        string again_;
        cout << "Do you want to try again? YES (y) or No (n)? >> ";
        cin >> again_;
        if (again_ == "n" || again_ == "q"){
          cout << "\nTHANKS FOR TRYING OUT MY GAME...\n";
          // stop = "y";
          break;
        } else {
          cout << "...";
        }

      }else{
        break;
        }
    }
}

string playerIfelse(string PLAYER){
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
  else if(PLAYER == "who"){
    cout << "me" << endl;
  }
  else{
    PLAYER = "invalid_input";
  }

  return PLAYER;
}

string computerIfelse(int CHOSEN){
  string COMPUTER;
  if (CHOSEN == 1){
    COMPUTER = "Rock";
  }
  else if (CHOSEN == 2){
    COMPUTER = "Paper";
  }   
  else if (CHOSEN == 3){
    COMPUTER = "Scissors";
  }     
  else if (CHOSEN == 4){
    COMPUTER = "Lizard";
  }
  else{
    COMPUTER = "Spock";
  }
  return COMPUTER;
}

string outcomeIfelse(string PLAYER, string COMPUTER){
  string OUTCOME;
  if (PLAYER == "who"){
    OUTCOME = "\
        _|_|          _|_|_|    _|_|    _|      _|  _|_|_|_|      _|      _|    _|_|    _|_|_|    _|_|_|_|      _|_|_|    _|      _| \n\
      _|    _|      _|        _|    _|  _|_|  _|_|  _|            _|_|  _|_|  _|    _|  _|    _|  _|            _|    _|    _|  _| \n\
      _|_|_|_|      _|  _|_|  _|_|_|_|  _|  _|  _|  _|_|_|        _|  _|  _|  _|_|_|_|  _|    _|  _|_|_|        _|_|_|        _| \n\
      _|    _|      _|    _|  _|    _|  _|      _|  _|            _|      _|  _|    _|  _|    _|  _|            _|    _|      _| \n\
      _|    _|        _|_|_|  _|    _|  _|      _|  _|_|_|_|      _|      _|  _|    _|  _|_|_|    _|_|_|_|      _|_|_|        _|    _| \n\
                                                                                                                                  _| \n\
      _|      _|    _|_|    _|    _|    _|_|    _|      _|  _|      _|    _|_|    _|_|_|        _|_|_|    _|_|_|  _|          _|_|    _|      _| \n\
      _|_|  _|_|  _|    _|  _|    _|  _|    _|  _|_|  _|_|  _|_|  _|_|  _|    _|  _|    _|        _|    _|        _|        _|    _|  _|_|  _|_| \n\
      _|  _|  _|  _|    _|  _|_|_|_|  _|_|_|_|  _|  _|  _|  _|  _|  _|  _|_|_|_|  _|    _|        _|      _|_|    _|        _|_|_|_|  _|  _|  _| \n\
      _|      _|  _|    _|  _|    _|  _|    _|  _|      _|  _|      _|  _|    _|  _|    _|        _|          _|  _|        _|    _|  _|      _| \n\
      _|      _|    _|_|    _|    _|  _|    _|  _|      _|  _|      _|  _|    _|  _|_|_|        _|_|_|  _|_|_|    _|_|_|_|  _|    _|  _|      _|  ";
  }

  // outcomes
  else if (PLAYER == COMPUTER){
    OUTCOME = "It\"s a DRAW!";
  }
  else if (PLAYER == "Rock" && COMPUTER == "Scissors"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Rock" && COMPUTER == "Paper"){
    OUTCOME = "COMPUTER wins!";
  }
  else if (PLAYER == "Rock" && COMPUTER == "Lizard"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Rock" && COMPUTER == "Spock"){
    OUTCOME = "COMPUTER wins!";
  }

  else if (PLAYER == "Paper" && COMPUTER == "Rock"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Paper" && COMPUTER == "Scissors"){
    OUTCOME = "COMPUTER wins!";
  }
  else if (PLAYER == "Paper" && COMPUTER == "Spock"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Paper" && COMPUTER == "Lizard"){
    OUTCOME = "COMPUTER wins!";
  }

  else if (PLAYER == "Scissors" && COMPUTER == "Paper"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Scissors" && COMPUTER == "Rock"){
    OUTCOME = "COMPUTER wins!";
  }
  else if( PLAYER == "Scissors" && COMPUTER == "Lizard"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Scissors" && COMPUTER == "Spock"){
    OUTCOME = "COMPUTER wins!";
  }

  else if (PLAYER == "Lizard" && COMPUTER == "Paper"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Lizard" && COMPUTER == "Rock"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Lizard" && COMPUTER == "Scissors"){
    OUTCOME = "COMPUTER wins!";
  }
  else if (PLAYER == "Lizard" && COMPUTER == "Spock"){
    OUTCOME = "COMPUTER wins!";
  }

  else if (PLAYER == "Spock" && COMPUTER == "Paper"){
    OUTCOME = "COMPUTER wins!";
  }
  else if (PLAYER == "Spock" && COMPUTER == "Rock"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Spock" && COMPUTER == "Scissors"){
    OUTCOME = "PLAYER wins!";
  }
  else if (PLAYER == "Spock" && COMPUTER == "Lizard"){
    OUTCOME = "COMPUTER wins!";
  }
  else{
    OUTCOME = "Invalid user input, COMPUTER wins!";
  }

  return OUTCOME;
}