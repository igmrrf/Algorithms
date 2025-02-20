

#include <iostream>
#include <string>
#include <utility>
#include <vector>

typedef std::vector<std::pair<std::string, int>> pairlist_t;
typedef std::string text_t;

using pairlist_t = std::vector<std::pair<std::string, int>>;
using text_t = std::string;
// string int paired
enum Day {
  sunday = 1, // defaults to 0 except set
  monday,
  tuesday,
  wednesday,
  thursday,
  friday,
  saturday,
};

struct Car {
  std::string model;
  int year;
  std::string color;
};

int main() {
  // a pair of string-int in a hashmap
  text_t name = "The Lazy";
  std::cout << name;
  return 0;
}
