// Steps
// check for the values if within constraints then length
// return if n is a single digit and k = 1
// else loop with k as length and concat n.
// separate all values of n and add
// if the length is one return else call the function again.

function superDigit(n, k) {
	console.log({ n, k });
	let newN = n;
	let newK = k;
	if (!n || n < 1 || n > 10e1000) {
		throw new Error("Invalid value for n");
	}
	if (!k || k < 1 || k > 10e5) {
		throw new Error("Invalid value for k");
	}

	if (n < 10) {
		newN = n * k;
		newK = 1;
	}
	if (newN < 10 && newK === 1) {
		return n;
	}
	let total = 0;
	const nums = newN.toString().split("");
	for (const num of nums) {
		total += Number(num);
	}
	return superDigit(total, newK);
}

// takes g and n from terminal and cals the function with each number expecting multiple print
// 1<= g <= 1000
// 1<= n <= 10e5
// 1<= n <= 10000 for 50% of the maxium score
// Alice always goes first (odd player)
// Bob always falls in as the even player
// run a lop to create the set of numbers into an array or set
// check for the best prime number, given it'll be the smaller number,
// we start from the left ignoring 1
// take the number and divid through the rest, if any is completely divisible, remove that number,
// and the number used to handle the division
// set prime to true and increase the number of plays
// if the number isn't dvisible by any still remove the number
function sillyGame3(n) {
	const set = new Set();
	for (let i = 1; i <= n; i++) {
		set.add(i);
	}
	function getPrime(arry, oldPlays, oldLast) {
		const values = [...arry.values()];
		plays = oldPlays || 0;
		last = oldLast || values[values.length - 1];
		const size = values.length;
		if (size === 1) {
			if (plays === 0) {
				return `Bob ${last}`;
			}
			const result = plays % 2;
			if (result === 1) {
				return `Alice ${last}`;
			}
			return `Bob ${last}`;
		}
		// select the biggest  prime number
		const num = values[1];

		for (let i = 1; i < size; i++) {
			if (values[i] % num === 0) {
				arry.delete(values[i]);
			}
		}

		return getPrime(arry, plays + 1, last);
	}

	return getPrime(set);
}

function sillyGame1(n) {
	let set = new Set();
	for (let i = 1; i <= n; i++) {
		set.add(i);
	}
	let plays = 0;
	let oldSize;

	while (set.size > 1) {
		const values = [...set.values()];
		const size = values.length;
		const num = values[1];

		for (let i = 1; i < size; i++) {
			if (values[i] % num === 0) {
				set.delete(values[i]);
			}
		}
		if (n > 1000 && oldSize - size === 1) {
			plays += size;
			set = new Set([1]);
		} else {
			plays += 1;
		}
	}

	if (plays % 2 === 1) {
		return "Alice";
	}
	return "Bob";
}

function sillyGame2(n) {
	// Initialize the array to keep track of prime factors
	const isPrime = new Array(n + 1).fill(true);
	isPrime[0] = isPrime[1] = false;

	let primeFactors = 0;
	// Sieve of Eratosthenes: Mark non-prime numbers
	for (let i = 2; i <= n; i++) {
		if (isPrime[i]) {
			primeFactors++;
			for (let j = i * i; j <= n; j += i) {
				isPrime[j] = false;
			}
		}
	}

	// Determine the winner based on the number of prime factors
	if (primeFactors % 2 === 1) {
		return "Alice";
	}
	return "Bob";
}

const hundred = new Array(10000)
	.fill(1, 0, 10000)
	.map((value, index) => index + 900000);

// const start = performance.now();
// hundred.forEach((n) => {
//   sillyGame2(n);
// });
// const done = performance.now();
// console.log({ dif: done - start });

module.exports = { sillyGame2 };
