function mean() {
  return Object.values(arguments).reduce((s,c) => s+c, 0) / arguments.length;
}