#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>

void happybirthday(std::string name, int age) {
  std::cout << "happybirthday to you " << name << " \n";
  std::cout << "happybirthday to you \n";
  std::cout << "happybirthday to dear \n";
  std::cout << "happybirthday to you \n";
  std::cout << "happybirthday to you " << age << "\n";
}

std::string concatnameage(std::string name, int age) {
  std::string newage = std::to_string(age);
  return name + " " + newage;
}

void bakePizza();
void bakePizza(std::string topppings);

void is_an_adult(int age);

int main() {
  std::string name = "bro";
  int age = 23;
  bakePizza();
  bakePizza("Peperoni");
  happybirthday(name, age);
  concatnameage(name, age);
  return 0;
}

void is_and_adult(int age) {
  if (age > 18) {
    std::cout << "you're an adult\n";
  }
}

void bakePizza() { std::cout << "here is your pizza!\n"; }

void bakePizza(std::string toppings) {
  std::cout << "Here is your" << toppings << " Pizza \n";
}
