#include <iostream>
#include <string>

int main() {
  int rows;
  int columns;
  char symbol;
  std::cout << "************* Triangle Generator ************* \n";
  std::cout << "How many rows?: ";
  std::cin >> rows;

  // std::cout << "How many columns?: ";
  // std::cin >> columns;

  std::cout << "Enter a symbol to use: ";
  std::cin >> symbol;

  for (int i = 1; i <= rows; i++) {
    if (i % 2) {
      int spaces = (rows - i) / 2;
      std::string empty;
      for (int k = 1; k <= spaces; k++) {
        empty.append(" ");
      }
      std::cout << empty;
      for (int j = 1; j <= i; j++) {
        std::cout << symbol;
      }
      std::cout << empty;

      std::cout << "\n";
    }
  }
  std::cout << "\n";
  std::cout << "************* Triangle Generator *************";
  return 0;
}
