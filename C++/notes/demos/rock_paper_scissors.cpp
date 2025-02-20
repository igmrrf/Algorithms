#include <cstdlib>
#include <cstring>
#include <iostream>

char get_user_choice();
char get_computer_choice();
void show_choice(char choice);
void choose_winner(char player, char computer);

int main() {

  char player = get_user_choice();
  std::cout << "You choice: ";
  show_choice(player);

  char computer = get_computer_choice();
  std::cout << "Computer's choice: ";
  show_choice(computer);

  choose_winner(player, computer);

  return 0;
}

char get_user_choice() {
  char player;
  const char choices[] = "rps";
  std::cout << "Rock-Paper-Scissors Game!\n";
  std::cout << "****************************\n";
  do {
    std::cout << "Choose one of the following!\n";

    std::cout << "****************************\n";
    std::cout << "r for rock\n";

    std::cout << "p for paper\n";
    std::cout << "s for scissors\n";

    std::cin >> player;

  } while (!std::strchr(choices, player));

  return player;
}
char get_computer_choice() {
  char play;
  srand(time(NULL));
  char choices[] = {'p', 'r', 's'};

  int choice = (rand() % 3);
  play = choices[choice];

  return play;
}
void show_choice(char choice) {
  switch (choice) {
  case 'r':
    std::cout << "Rock\n";
    break;
  case 'p':
    std::cout << "Paper\n";
    break;
  case 's':
    std::cout << "Scissors\n";
    break;
  default:
    std::cout << " Invalid Choice\n";
    break;
  }
};
void choose_winner(char player, char computer) {

  if (player == computer) {
    std::cout << "Draw Lets try again";
    return;
  }
  switch (player) {
  case 'r':
    switch (computer) {
    case 'p':
      std::cout << "Computer wins\n";
      break;
    case 's':
      std::cout << "Player wins\n";
      break;
    }
    break;

  case 'p':
    switch (computer) {
    case 'r':
      std::cout << "Player wins\n";
      break;
    case 's':
      std::cout << "Computer wins\n";
      break;
    }
    break;

  case 's':
    switch (computer) {
    case 'r':
      std::cout << "Computer wins\n";
      break;
    case 'p':
      std::cout << "Player wins\n";
      break;
    }
    break;

  default:

    break;
  }
};
