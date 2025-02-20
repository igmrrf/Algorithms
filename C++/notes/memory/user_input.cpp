

#include <iostream>
#include <istream>
#include <string>

int main() {
  std::string name;
  short age;

  std::cout << "What's your full name?: ";
  // std::getline(std::cin, name); // take in spaced string
  // P.S: getline after a cin will take in the '\n' defaultly sent
  // by cin skipping it's input, thats why we use whats below
  std::getline(std::cin >> std::ws, name);

  std::cout << "What's your age?: ";
  std::cin >> age;

  std::cout << "Hello " << name << "\n";
  std::cout << "You are " << age << "years old";
  return 0;
}
