var subtractProductAndSum = function (n) {
  let arr = n.toString().split("").map((digit) => parseInt(digit));
  let product = 1;
  let sum = 0;
  for (i = 0; i < arr.length; i++) {
    product *= arr[i];
    sum += arr[i];
  }
  return product - sum;
};


