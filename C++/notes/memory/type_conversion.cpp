#include <iostream>

int main() {
  // a pair of string-int in a hashmap
  int students = 20;
  // implicit
  int x = 3.14; // x = 3
  // explicit
  double y = (int)3.141;
  std::cout << y; // y = 3
  students += 1;

  // implicit
  char z = 100;
  std::cout << z; // z = d;

  // explicit
  std::cout << (char)100; // d;
                          // example
  int correct = 8;
  int questions = 10;
  double score = correct / questions * 100;          // score = 0
  double score2 = correct / (double)questions * 100; // score = 80
  return 0;
}
