
#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>

// Luhn Algorithm
// 1. Double every second digit from right to left, if doubled number is 2
// digits, split
// 2. Add all single digits from step 1
// 3. Add all odd placed number digits from right to left
// 4. Sum results from steps 2 and 3
// 5. If step 4 is divisible by 10, # is valid;
int get_digit(const int number);
int sum_odd_digits(const std::string card_number);
int sum_even_digits(const std::string card_number);
int main() {
  // or take input from user
  int result = 0;
  std::string card_number = "6011000990139424";
  result = sum_odd_digits(card_number) + sum_even_digits(card_number);
  std::cout << result << "\n";

  if (result % 10 == 0) {
    std::cout << "Valid card number" << "\n";
  } else {
    std::cout << "invalid card number" << "\n";
  }

  return 0;
}

int get_digit(const int number) {
  // 4
  // 4%10 = 4 + number/10 (0)%10 = 4
  return number % 10 + (number / 10 % 10);
};

int sum_odd_digits(const std::string card_number) {
  int sum = 0;
  for (int i = card_number.size() - 1; i >= 0; i -= 2) {
    sum += get_digit(card_number[i] - '0');
  }
  std::cout << "SUM ODD: " << sum << "\n";

  return sum;
};

int sum_even_digits(const std::string card_number) {
  int sum = 0;
  for (int i = card_number.size() - 2; i >= 0; i -= 2) {
    sum += get_digit((card_number[i] - '0') * 2);
  }
  std::cout << "EVEN ODD: " << sum << "\n";

  return sum;
};
