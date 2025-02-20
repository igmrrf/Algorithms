
#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>

int main() {
  std::string questions[] = {
      "1. What year was C++ created?: ", "2. Who invented C++?: ",
      "3. What is the predecessor of C++?: ", "4. Is the Earth flat?: "};
  std::string options[][4] = {
      {"A. 1969", "B. 1975", "C. 1985", "D. 1989"},
      {"A. Guido van Rossum", "B. Bjarne Stroustrup", "C. John Carmick",
       "D. Mark Zuckerburg"},
      {"A. C", "B. C+", "C. C--", "D. B++"},
      {"A. Yes", "B. No.", "C. Sometimes", "D. What's Earth?"},
  };
  char answer_keys[] = {'C', 'B', 'A', 'B'};
  int size = sizeof(questions) / sizeof(questions[0]);
  char guess;
  int score = 0;

  // go through the array and output in the form of the array
  for (int i = 0; i < size; i++) {
    std::cout << "******************************************\n";
    std::cout << questions[i] << "\n";
    std::cout << "******************************************\n";
    int option_size = sizeof(options[0]) / sizeof(options[0][0]);
    for (int j = 0; j < option_size; j++) {
      std::cout << options[i][j] << "\n";
    };
    std::cout << "Guess: ";
    std::cin >> guess;

    guess = toupper(guess);

    if (guess == answer_keys[i]) {
      std::cout << "CORRECT\n";
      score++;
    } else {
      std::cout << "WRONG\n";
      std::cout << "Answer: " << answer_keys[i] << "\n";
    }
  };

  std::cout << "******************************************\n";
  std::cout << "******************RESULT******************\n";
  std::cout << "******************************************\n";
  std::cout << "CORRECT GUESSES: " << score << "\n";
  std::cout << "# of QUESTIONS" << size << "\n";
  std::cout << "SCORE: " << (score / (double)size) * 100 << "%";
  return 0;
}
