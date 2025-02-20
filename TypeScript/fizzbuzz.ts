function fizzbuzz(num: number) {
	if (typeof num !== "number") {
		return "parameter must be a number";
	}
	if (num === 0) {
		return "parameter must be a natural number";
	}

	if (num % 3 === 0 && num % 5 === 0) {
		return "fizzbuzz";
	} else if (num % 3 === 0) {
		return "fizz";
	} else if (num % 5 === 0) {
		return "buzz";
	}
	return "invalid num";
}
console.log(fizzbuzz(15));
console.log(fizzbuzz(3));
console.log(fizzbuzz(4));
