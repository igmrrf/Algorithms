function shuffle(newAnwsers: Array<string>) {
  let currentIndex = newAnwsers.length,
    randomIndex;
  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;
    [newAnwsers[currentIndex], newAnwsers[randomIndex]] = [newAnwsers[randomIndex], newAnwsers[currentIndex]];
  }
  return newAnwsers;
}
