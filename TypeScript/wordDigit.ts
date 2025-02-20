const word = "turing";

function DigitizeWord(str: string) {
    let sum = 0;
    for (const alphabet of str) {
        sum += alphabet.charCodeAt(0) - 97;
    }
    let result = 0;
    while (sum > 0 || result > 9) {
        if (sum == 0) {
            sum = result;
            result = 0;
        }
        result += sum % 10;
        sum = Math.floor(sum / 10);
    }
    return result;
}

// return 8
console.log(DigitizeWord(word));
