#include <iostream>
int add_ints_between(int start, int end);
void program();

int main() {
  int start;
  int end;
  program();
  return 0;
}
void program() {
  int start;
  int end;
  int sum;
  std::cout << "Sum: " << sum << "\n";
  std::cout << "************ Sum Between Two Numbers **************\n";
  std::cout << "Enter first number(start): ";
  std::cin >> start;

  std::cout << "Enter second number(end): ";
  std::cin >> end;

  std::cout << "************ Sum Between Two Numbers **************\n";
  int result = add_ints_between(start, end);
  std::cout << "The sum of numbers between " << start << " and " << end
            << " is " << result;
};

int add_ints_between(int start, int end) {
  if (end < start) {
    std::cout << "End should be greater than than the start";
    return 0;
  }
  if (end == 0) {
    std::cout << "End should be greater than zero";
  }

  int range = end - start;
  int sum = 0;
  for (int i = 0; i <= range; i++) {
    int num = start + i;
    int result = 0;
    do {
      sum += num % 10;
      result = num / 10;
      num = result;
    } while (result);
  }
  return sum;
};
