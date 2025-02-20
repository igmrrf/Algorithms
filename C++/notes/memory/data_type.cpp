
#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <cstring>

template <typename T> T max(T x, T y);

template <typename T, typename U> U min(T x, U y);

int main() {
  max('1', '2');
  max(1, 2);

  min('1', '2');
  min(1, 2.1);
  return 0;
}
