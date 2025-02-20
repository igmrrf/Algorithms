

#include <iostream>

int main() {
  int age;
  std::cout << "Enter your age: ";
  std::cin >> age;
  if (age >= 18) {
    std::cout << "Welcome to the site";
  } else {
    std::cout << "You're not old enough";
  }

  int month;
  std::cout << "Enter your birth month: ";
  std::cin >> month;

  switch (month) {
  case 1:
    std::cout << "It is January";
    break;
  default:
    break;
  }

  int grade = 75;
  int attendance = 70;

  grade >= 60 ? std::cout << "You pass!!" : std::cout << "You fail";

  std::cout << (grade <= 20 ? "You failed" : "You tried");

  std::cout << (grade >= 70 && attendance >= 70 ? "Excelent" : "Try harder");

  std::cout << (grade >= 70 || attendance >= 70 ? "Excelent" : "Try harder");

  std::cout << (grade != 70 && attendance != 70
                    ? "Please work on your grade and attendance"
                    : "You're working hard");

  return 0;
}
