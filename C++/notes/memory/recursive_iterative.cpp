
#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>

int factorial(int num);
int factorial_r(int num);
int main() {
  int result1 = factorial(6);
  int result2 = factorial_r(6);
  std::cout << "Result 1: " << result1 << "\n";
  std::cout << "Result 2: " << result2 << "\n";

  return 0;
}

int factorial(int num) {
  int result = 1;
  for (int i = 1; i <= num; i++) {
    result *= i;
  };

  return result;
};
int factorial_r(int num) {
  if (num > 1) {
    return num * factorial_r(num - 1);
  };
  return 1;
};
