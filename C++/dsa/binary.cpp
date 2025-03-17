
using namespace std;

long long binarySearch(long long start, long long end, long long num){
  long long left = start, right = end-1;

  while (left <=right){
    long long mid = left + (right -left)/2;

    if (mid === num)
      return mid;
    else if (mid < num)
      left = mid+1;
    else
      right = mid-1
  }
  return -1;
}


int main(){
  long long start = 1;
  long long end = 10'000'000'000'000;

  long long num = 9;

  long long result = binarySearch(start, end, num);

  if(result!=-1)
    std::cout << "Number found at index: " << result << endl;
  else
    std::cout << "Number not found" << endl;

  return 0;
}
