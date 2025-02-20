
#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>

class Human {

private:
  std::string planet = "Earth";
  std::string galaxy = "Milky way";
  int temperature = 0;

  void digest() { std::cout << "This person is digesting \n"; };

public:
  std::string name = "Rick";
  std::string country;
  std::string gender;
  std::string occupation;
  std::string mobile;
  int age;

  // constructor
  Human() {};

  // constructor
  Human(int temperature) { this->set_temperature(temperature); };

  // constructor
  Human(std::string country, std::string gender) {
    this->country = country;
    this->gender = gender;
  }

  // constructor
  // constructor overloading
  Human(std::string country, std::string gender, std::string phone_number) {
    this->country = country;
    this->gender = gender;
    // if different name, you can directly set the value;
    mobile = phone_number;
  }

  std::string get_planet() { return planet; };

  int get_temperature() { return temperature; };

  int set_temperature(int temperature) {
    if (temperature < 0) {
      this->temperature = 0;
    } else if (temperature >= 100) {
      this->temperature = 100;
    } else {
      this->temperature = temperature;
    }
    return this->temperature;
  };

  void eat() { std::cout << "This person is eating \n"; };

  void drink() { std::cout << "This person is drinking \n"; };

  void sleep() { std::cout << "This person is sleeping \n"; };
};

class Dentis : public Human {
private:
  const std::string occupation = "Dentist";

public:
  std::string get_occupation() { return this->occupation; };
};

class Programmer : private Human {
private:
  const std::string occupation = "Programmer";

public:
  std::string get_occupation() { return this->occupation; };
  std::string planet = this->get_planet();
};

int main() {
  Human human1("Nigeria", "Male", "+23481818181818");
  Human human2("Nigeria", "Male");
  Human human3;
  Human human4(75);

  human1.name = "Rick";
  human1.occupation = "Scientist";
  human1.age = 23;

  human1.eat();
  human1.drink();
  human1.sleep();

  Dentis dentist1;
  std::string occupation = dentist1.get_occupation();
  std::string planet = dentist1.get_planet();
  std::cout << "Human is a: " << occupation << "\n";

  Programmer programmer1;
  std::string programmer_occcupation = programmer1.get_occupation();
  std::string programmer_planet = programmer1.planet;

  std::cout << "Human is a: " << programmer_occcupation << "\n";
  std::cout << "Human is in: " << programmer_planet << "\n";
  return 0;
}
