const sumTwoSmallest = (numbers) => {
  numbers.sort((a, b) => a - b);
  return numbers[0] + numbers[1];
};

console.log(sumTwoSmallest([3, 90, 2, 45, 11, 4, 11, 332]));
