
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>

std::string get_foods(int size);

int main() {
  const int SIZE = 5;
  std::string foods[SIZE];
  int size = sizeof(foods) / sizeof(foods[0]);
  std::string temp;
  for (int i = 0; i < size; i++) {
    std::cout << "Enter a food you like #" << i + 1 << ": ";
    std::getline(std::cin, temp);
    if (temp == "q") {
      break;
    }
    foods[i] = temp;
  }
  std::cout << "You like the following foods:\n";
  return 0;
}

std::string get_foods(int size) {
  srand(time(NULL));
  int extra = rand();

  return "pizza_" + std::to_string(extra);
};
