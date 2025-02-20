#include <__chrono/duration.h>
#include <cfloat>
#include <climits>
#include <iostream>
#include <string>
int main() {
  // Welcome text on separate lin
  std::cout << "Hello World\n" << "This will show up in a new line";
  // Sum two numbers
  short sum = 29 + 30;
  std::cout << "29+30=" << sum << "\n";
  // size of fundamental data types

  short char_size = sizeof(char);
  short bool_size = sizeof(bool);
  short short_size = sizeof(short);
  short int_size = sizeof(int);
  short long_size = sizeof(long);
  short long_long_size = sizeof(long long);
  short long_double_size = sizeof(long double);
  short float_size = sizeof(float);
  short double_size = sizeof(double);

  std::cout << "The size of (char) is: " << char_size << " bytes" << "\n";
  std::cout << "The size of (bool) is: " << bool_size << " bytes" << "\n";
  std::cout << "The size of (long double) is: " << long_double_size << " bytes"
            << "\n";
  // Sum using variables
  short variableA = 29;
  short variableB = 30;
  short result = variableA + variableB;

  std::cout << "variableA + variableB = " << result << "\n";

  std::cout << "The minimum limit of int is: " << INT_MAX << "\n";
  std::cout << "The minimum limit of short is: " << SHRT_MAX << "\n";
  std::cout << "The minimum limit of char is: " << CHAR_MAX << "\n";
  std::cout << "The minimum limit of long is: " << LONG_MAX << "\n";
  std::cout << "The minimum limit of long long is: " << LLONG_MAX << "\n";
  std::cout << "The minimum limit of long double is: " << LDBL_MAX << "\n";
  std::cout << "The minimum limit of double is: " << DBL_MAX << "\n";
  std::cout << "The minimum limit of float is: " << FLT_MAX << "\n";

  std::string name = "The Lazy";
  std::cout << "Hello, " << name << ". How are you?";

  return 0;
}
