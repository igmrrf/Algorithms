const { parentPort } = require("worker_threads");
const { sillyGame2 } = require(".");
const now = performance.now();
parentPort.on("message", (jobs) => {
  jobs.forEach((element) => {
    sillyGame2(element);
  });
  console.log({ diff1: performance.now() - now });
  parentPort.postMessage("done");
});
