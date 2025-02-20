
#include <iostream>
#include <string>

char get_user_choice();
char get_computer_choice();
void show_choice(char choice);
void choose_winner(char player, char computer);

int main() {
  char player;
  char computer;
  int start;
  int end;
  std::string time = "12:01AM to 12:00PM:";
  int firstColumn = time.find_first_of(":");
  std::string fisrtHr = time.substr(0, firstColumn);
  std::string fisrtType = time.substr(firstColumn + 3, 2);
  std::string fisrtminute = time.substr(firstColumn + 1, 2);

  int secondColumn = time.find(":", 4);
  std::string secondHour = time.substr(secondColumn - 2, 2);
  std::string secondMinute = time.substr(secondColumn + 1, 2);
  std::string secondType = time.substr(secondColumn + 3, 2);

  int numfirstHr = std::stoi(fisrtHr);
  int numsecondHr = std::stoi(secondHour);
  int numfirstMinute = std::stoi(fisrtminute);
  int numsecondMinute = std::stoi(secondMinute);
  int diffToAdd = 0;
  if (secondType != fisrtType) {
    diffToAdd = 12;
    if (numfirstHr > numsecondHr) {
      diffToAdd = 24;
    }
  }
  int hourDiff = (numsecondHr + diffToAdd) - numfirstHr;
  std::cout << "minute Diff: " << hourDiff << "\n";
  int diffMinutes =
      ((((numsecondHr + diffToAdd) - numsecondHr) * 60) + numsecondMinute) -
      numfirstMinute;
  std::cout << "minute Diff: " << diffMinutes << "\n";
  return 0;
}

char get_user_choice() { return 0; }
char get_computer_choice() { return 0; }
void show_choice(char choice);
void choose_winner(char player, char computer);
