
#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
  srand(time(0));
  short num;
  short guess;
  short tries = 0;

  num = (rand() % 100) + 1; // random with limt of 5-1
  std::cout << "*********** Number Guessing Game *************\n";
  do {
    std::cout << "Guess the Number: ";
    std::cin >> guess;

    tries += 1;
    if (guess > num) {
      std::cout << "Ops, Too high!\n";
    } else if (guess < num) {
      std::cout << "Ops, Too low!\n";
    } else {

      std::cout << "Correct, # of tries: " << tries << "\n";
    }
  } while (guess != num);

  std::cout << "*********** Number Guessing Game *************\n";
  return 0;
}
