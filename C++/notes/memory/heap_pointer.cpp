
#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>

int main() {
  int *p_num = NULL;

  p_num = new int;

  *p_num = 21;

  std::cout << "Address: " << p_num << "\n";
  std::cout << "Value: " << *p_num << "\n";

  delete p_num;

  char *p_grades = NULL;
  int size;

  std::cout << "How many grades to enter in?: ";
  std::cin >> size;

  p_grades = new char[size];

  for (int i = 0; i < size; i++) {
    std::cout << "Enter grage #" << i + 1 << ": ";
    std::cin >> p_grades[i];
  }

  for (int i = 0; i < size; i++) {
    std::cout << p_grades[i] << " ";
  }
  delete[] p_grades;
  return 0;
}
