const isDivisibleBy = (a, b) => a % b === 0;

export default year => {
  if(isDivisibleBy(year, 100)) return isDivisibleBy(year, 400);
  else return isDivisibleBy(year, 4);
}
