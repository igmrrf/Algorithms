const Arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
const Arr2 = ["a", "b", "c"];

function createTree(longArray, shortArray) {
	let position = 0;
	for (let i = 0; i < Arr1.length; i++) {
		console.log({ Number: Arr1[i], Letter: Arr2[position] });
		position++;
		if ((i + 1) % shortArray.length === 0) position = 0;
	}
}

createTree(Arr1, Arr2);

// NOTE: Function Composition
const compose = (f, g) => (x) => f(g(x));

const f = (num: number) => num * 2;
const g = (num: number) => num + 1;

const h = compose(f, g);

console.log({ h: h(30) });
