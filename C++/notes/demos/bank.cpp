
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <ios>
#include <iostream>

void show_balance(double balance);
double deposit();
double withdraw(double balance);
int main() {

  double balance = 0;
  int choice = 0;
  do {
    std::cout << "*********************\n";
    std::cout << "Enter your choice: \n";
    std::cout << "*********************\n";
    std::cout << "1. Show Balance \n";
    std::cout << "2. Deposit Money \n";
    std::cout << "3. Withdraw Money \n";
    std::cout << "4. Exit \n";
    std::cin >> choice;

    std::cin.clear();
    fflush(stdin);

    switch (choice) {
    case 1:
      show_balance(balance);
      break;
    case 2:
      balance += deposit();
      break;
    case 3:
      balance -= withdraw(balance);
      break;
    case 4:
      std::cout << "Thanks for visiting!\n";
      break;
    default:
      std::cout << "Invalid Choice\n";
      break;
    }

  } while (choice != 4);

  return 0;
}

void show_balance(double balance) {
  std::cout << "Your balance is: $" << std::setprecision(2) << std::fixed
            << balance << "\n";
}

double deposit() {
  double amount = 0;
  std::cout << "Enter amount to be deposited: ";
  std::cin >> amount;
  if (amount > 0) {
    return amount;
  }
  std::cout << "That's not a valid amount";
  return amount;
}

double withdraw(double balance) {
  double amount = 0;
  std::cout << "Enter amount to be withdraw: ";
  std::cin >> amount;

  if (amount > balance) {
    std::cout << "Insufficient funds\n";
    return amount;
  }
  if (amount > 0) {
    return amount;
  }
  std::cout << "That's not a valid amount";
  return amount;
}
