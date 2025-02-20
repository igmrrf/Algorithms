let count = 0;
const t1 = performance.now();
function ackman(m: number, n: number): number {
  count++;
  let ans;
  if (m === 0) ans = n + 1;
  else if (n === 0) ans = ackman(m - 1, 1);
  else ans = ackman(m - 1, ackman(m, n - 1));

  return ans;
}

console.log('Ackman [4,1]: ', ` `, count);

const t2 = performance.now();
console.log('Time Taken: ', t2 - t1);

export default ackman;
