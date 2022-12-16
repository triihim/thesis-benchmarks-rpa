function mean() {
  return Object.values(arguments).reduce((s,c) => s+c, 0) / arguments.length;
}

function diff(a, b) {
  const best = a < b ? a : b;
  const value = a < b ? b : a;
  return parseFloat((value - best) / best * 100, 2).toFixed(2);
}