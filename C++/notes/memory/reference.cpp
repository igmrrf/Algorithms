
#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>

void swap_by_reference(std::string &x, std::string &y);
void swap_by_value(std::string x, std::string y);
int main() {
  std::string x = "Kool-Aid";
  std::string y = "Water";

  std::cout << "X: " << x << "\n";
  std::cout << "Y: " << y << "\n";

  std::cout << "X: " << &x << "\n";
  std::cout << "Y: " << &y << "\n";

  swap_by_reference(x, y);

  std::cout << "Reference X: " << x << "\n";
  std::cout << "Reference Y: " << y << "\n";

  swap_by_value(x, y);

  std::cout << "Value X: " << x << "\n";
  std::cout << "Value Y: " << y << "\n";

  return 0;
}
void swap_by_value(std::string x, std::string y) {

  std::cout << "Value Address X: " << &x << "\n";
  std::cout << "Value Address Y: " << &y << "\n";
  std::string temp;
  temp = x;
  x = y;
  y = temp;
};

void swap_by_reference(std::string &x, std::string &y) {

  std::cout << "Reference Address X: " << &x << "\n";
  std::cout << "Reference Address Y: " << &y << "\n";
  std::string temp;
  temp = x;
  x = y;
  y = temp;
};
