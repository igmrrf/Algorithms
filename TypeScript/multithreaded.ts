const { Worker } = require("worker_threads");

const share = (arr, n) => {
  const chunks = [];
  for (let i = n; i > 0; i--) {
    chunks.push(arr.splice(0, Math.ceil(arr.length / i)));
  }
  console.log({ chunks: chunks[0].length });
  return chunks;
};
const hundred = new Array(10000)
  .fill(1, 0, 10000)
  .map((value, index) => index + 900000);

function solve(jobs, workers) {
  const chunks = share(jobs, workers);

  const start = performance.now();
  let completedWorkers = 0;
  chunks.forEach((data, i) => {
    const worker = new Worker("./worker.js");
    worker.postMessage(data);
    worker.on("message", (message) => {
      console.log(`Worker ${i} finished`);
      completedWorkers++;
      if (completedWorkers === workers) {
        console.log(`All workers finished in ${performance.now() - start} ms`);
        process.exit();
      }
    });
  });
}

solve(hundred, 5);
