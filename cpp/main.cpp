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
  
*/

#include <iostream>
#include <string>
#include <ctime>

using namespace std;

void game();
string playerIfelse(string);
string computerIfelse(int);
string outcomeIfelse(string, string);

int main()
{

  system("cls");
  cout << "\nA GAME MADE BY MOHAMMAD ISLAM\n* The purpose of this program is to\
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
  \n /__/    /__/    /__/ "
       << endl;

  game();
}

// defination of the whole game
static string stop = "n";

void game()
{
  srand(time(0));
  // initial stop set to nothing
  string p_choice;

  while (stop == "n")
  {
    // stop = "y";
    // asks the player input
    cout << "\n\nWhat do you want to play? \n[r]ock, [p]aper, [s]cissors, [l]izard, [sp]ock? >> ";
    cin >> p_choice;

    if (p_choice != "q")
    {
      string PLAYER = playerIfelse(p_choice);

      // computer random choise
      string COMPUTER = computerIfelse(rand() % 5);

      // Result
      cout << "PLAYER"
           << " vs. "
           << "COMPUTER" << endl;
      cout << PLAYER << " vs. " << COMPUTER << endl;

      // Outcomes
      string OUTCOME = outcomeIfelse(PLAYER, COMPUTER);
      cout << OUTCOME << endl;

      //Again
      string again_;
      cout << "Do you want to try again? YES (y) or No (n)? >> ";
      cin >> again_;
      if (again_ == "n" || again_ == "q")
      {
        cout << "\nTHANKS FOR TRYING OUT MY GAME...\n";
        // stop = "y";
        break;
      }
      else
      {
        cout << "...";
      }
    }
    else
    {
      break;
    }
  }
}

string playerIfelse(string PLAYER)
{

  if (PLAYER == "sp")
  {
    PLAYER = "Spock";
  }
  else if (PLAYER == "p")
  {
    PLAYER = "Paper";
  }
  else if (PLAYER == "l")
  {
    PLAYER = "Lizard";
  }
  else if (PLAYER == "s")
  {
    PLAYER = "Scissors";
  }
  else if (PLAYER == "r")
  {
    PLAYER = "Rock";
  }
  else if (PLAYER == "who")
  {
    cout << "me" << endl;
  }
  else
  {
    PLAYER = "invalid_input";
  }

  return PLAYER;
}

string computerIfelse(int CHOSEN)
{
  string COMPUTER;
  switch (CHOSEN)
  {
  case 1:
    COMPUTER = "Rock";
    break;
  case 2:
    COMPUTER = "Paper";
    break;
  case 3:
    COMPUTER = "Scissors";
    break;
  case 4:
    COMPUTER = "Lizard";
    break;
  case 5:
    COMPUTER = "Spock";
    break;
  default:
    COMPUTER = "ERROR";
    break;
  }
  return COMPUTER;
}

string outcomeIfelse(string PLAYER, string COMPUTER)
{
  string OUTCOME;
  if (PLAYER == "who")
  {
    OUTCOME = "\
   _                                                      _        _                     \n\
  /_\\     __ _  __ _ _ __ ___   ___   _ __ ___   __ _  __| | ___  | |__  _   _           \n\
 / _ \\   / _` |/ _` | '_ ` _ \\ / _ \\ | '_ ` _ \\ / _` |/ _` |/ _ \\ | '_ \\| | | |          \n\
/  _  \\ | (_| | (_| | | | | | |  __/ | | | | | | (_| | (_| |  __/ | |_) | |_| |          \n\
\\_/ \\_/  \\__, |\\__,_|_| |_| |_|\\___| |_| |_| |_|\\__,_|\\__,_|\\___|_|_.__/ \\__, |          \n\
  /\\/\\   |___/ |__   __ _ _ __ ___  _ __ ___   __ _  __| |   \\_   \\___| ||___/ _ __ ___  \n\
 /    \\ / _ \\| '_ \\ / _` | '_ ` _ \\| '_ ` _ \\ / _` |/ _` |    / /\\/ __| |/ _` | '_ ` _ \\ \n\
/ /\\/\\ \\ (_) | | | | (_| | | | | | | | | | | | (_| | (_| | /\\/ /_ \\__ \\ | (_| | | | | | |\n\
\\/    \\/\\___/|_| |_|\\__,_|_| |_| |_|_| |_| |_|\\__,_|\\__,_| \\____/ |___/_|\\__,_|_| |_| |_|\n";
  }

  // outcomes

  // draw
  else if (PLAYER == COMPUTER)
  {
    OUTCOME = "It\"s a DRAW!";
  }

  // other outcomes

  // player wins
  else if (
      PLAYER == "Rock" && COMPUTER == "Scissors" ||
      PLAYER == "Rock" && COMPUTER == "Lizard" ||
      PLAYER == "Paper" && COMPUTER == "Rock" ||
      PLAYER == "Paper" && COMPUTER == "Spock" ||
      PLAYER == "Scissors" && COMPUTER == "Paper" ||
      PLAYER == "Scissors" && COMPUTER == "Lizard" ||
      PLAYER == "Lizard" && COMPUTER == "Paper" ||
      PLAYER == "Lizard" && COMPUTER == "Rock" ||
      PLAYER == "Spock" && COMPUTER == "Rock" ||
      PLAYER == "Spock" && COMPUTER == "Scissors")
  {
    OUTCOME = "PLAYER wins!";
  }

  // computer wins
  else if (
      PLAYER == "Rock" && COMPUTER == "Paper" ||
      PLAYER == "Rock" && COMPUTER == "Spock" ||
      PLAYER == "Paper" && COMPUTER == "Scissors" ||
      PLAYER == "Paper" && COMPUTER == "Lizard" ||
      PLAYER == "Scissors" && COMPUTER == "Rock" ||
      PLAYER == "Scissors" && COMPUTER == "Spock" ||
      PLAYER == "Lizard" && COMPUTER == "Scissors" ||
      PLAYER == "Lizard" && COMPUTER == "Spock" ||
      PLAYER == "Spock" && COMPUTER == "Paper" ||
      PLAYER == "Spock" && COMPUTER == "Lizard")
  {
    OUTCOME = "COMPUTER wins!";
  }

  // else
  else
  {
    OUTCOME = "Invalid user input, COMPUTER wins!";
  }

  return OUTCOME;
}