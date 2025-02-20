
#include <cstdlib>
#include <cstring>
#include <iostream>

int main() {
  // Bubble Sort
  int arrs[] = {2, 5, 10, 3, 4, 8, 9, 1, 7, 6};
  int tries = 0;
  int size = sizeof(arrs) / sizeof(arrs[0]);
  for (int i = 0; i < size - 1; i++) {
    std::cout << "Current Position: " << i << "\n";
    for (int j = 0; j < size - i - 1; j++) {
      int current_i = arrs[j];
      int current_j = arrs[j + 1];

      if (current_i > current_j) {
        int temp = current_i;
        arrs[j] = current_j;
        arrs[j + 1] = temp;
      }
      tries += 1;
    }
  }

  for (int i = 0; i < size; i++) {
    std::cout << arrs[i] << " ";
  }
  std::cout << "Tries: " << tries << " \n";
  return 0;
}
