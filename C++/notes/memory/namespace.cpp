
// NameSpaces
#include <iostream>
// Namespace = provides a solution for preventing naming conflicts
// in large projects. each entity needs a unique name. A namespace
// allows for identically named entities as long as the namespaces are different
namespace first {
int x = 1;
};

// variable scope
int myNum = 3;

namespace second {
int x = 3;
};

int main() {
  int x = 0;
  int myNum = 2;
  std::cout << ::myNum; // global scope
  std::cout << first::x;
  std::cout << second::x;
  return 0;
}

int notmain() {
  using namespace first;
  // using the first namespace
  std::cout << x;
  std::cout << second::x;
  return 0;
}
