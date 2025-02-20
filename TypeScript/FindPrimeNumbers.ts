console.log("hi");

const findPrimeNumbers = (min: number, max: number) => {
	const primes: number[] = [];
	for (let i = min; i < max; i++) {
		let isPrime = i >= 2;
		for (let j = 2; j < i; j++) {
			if (i % j === 0) {
				isPrime = false;
				break;
			}
		}

		if (isPrime === true) {
			primes.push(i);
		}
	}
	return primes;
};

const primes = findPrimeNumbers(0, 10);
console.log({ primes });
