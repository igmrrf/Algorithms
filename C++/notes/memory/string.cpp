#include <iostream>
#include <string>

int main() {
  std::string name = "Francis";
  // std::cout << "Enter your name: ";
  // std::getline(std::cin, name);

  short length = name.length();
  if (length > 12) {
    std::cout << "Your name can't be over 12 characters";
  } else {
    std::cout << "Welcome, " << name << "\n";
  }

  bool empty = name.empty();
  std::cout << "Is name empty? " << empty << "\n";

  char index2 = name.at(2);
  std::cout << "At index 2 " << index2 << "\n";

  std::string email = name.append("@gmail.com");
  std::cout << "Email " << email << "\n";

  std::string insert = name.insert(0, "@");
  std::cout << "Inserted " << insert << "\n";

  name.erase(0, 1);
  std::cout << "Erase first letter: " << name << "\n";

  unsigned long capacity = name.capacity();

  std::cout << capacity << "\n";

  name.clear(); // clears the value in name
  std::cout << "Name is: " << name << "\n";

  return 0;
}
