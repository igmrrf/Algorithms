#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>

int main() {
  // Pointers
  std::string name = "Bro";
  std::string *p_name = &name;

  std::string pizzas[5] = {"pizza1", "pizza2", "pizza3", "pizza4", "pizza5"};

  std::string *p_pizzas = pizzas;
  std::cout << "p_name: " << p_name << "\n";
  std::cout << "*p_name: " << *p_name << "\n";

  std::cout << "pizzas: " << pizzas << "\n";
  std::cout << "*pizzas: " << *pizzas << "\n";

  std::cout << "p_pizzas: " << p_pizzas << "\n";
  std::cout << "*p_pizzas: " << *p_pizzas << "\n";
  // Null Pointer (nullptr)
  int *p_x = nullptr;

  int x = 123;
  p_x = &x;

  if (p_x == nullptr) {
    std::cout << "address was not assigned \n";
    std::cout << *p_x << "\n";
  } else {

    std::cout << "address was assigned \n";
    std::cout << *p_x << "\n";
  }

  return 0;
}
