
#include <algorithm>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>

std::string get_foods(int size);

int main() {

  const int SIZE = 99;
  std::string foods[SIZE];

  std::cout << foods << "\n";

  int index = 0;
  std::fill(foods, foods + (SIZE / 3), get_foods(SIZE));
  std::fill(foods + (SIZE / 3), foods + (SIZE / 3 * 2), get_foods(SIZE));
  std::fill(foods + (SIZE / 3 * 2), foods + SIZE, get_foods(SIZE));
  // for (int i = 0; i < SIZE; i++) {
  //   std::cout << foods[i] << "\n";
  // }
  return 0;
}

std::string get_foods(int size) {
  srand(time(NULL));
  int extra = rand();

  return "pizza_" + std::to_string(extra);
};
