
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>

int main() {
  // declare two dimensional array
  // you have to declare column size but no so much of row size
  std::string cars[][3] = {
      {"Camry", "Corrola", "Avalon"},
      {"Apus", "Liad", "Bree"},
      {"ES350", "ES300", "GX470"},
  };
  // get the no.s of row and columns
  int rows = sizeof(cars) / sizeof(cars[0]);
  int columns = sizeof(cars[0]) / sizeof(cars[0][0]);

  // go through the array and output in the form of the array
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < rows; j++) {
      std::cout << cars[i][j] << " ";
    };
    std::cout << "\n";
  };
  return 0;
}
