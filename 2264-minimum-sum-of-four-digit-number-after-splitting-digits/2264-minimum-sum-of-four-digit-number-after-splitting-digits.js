var minimumSum = function (num) {
  let arr = num.toString().split("");
  arr.sort((a, b) => a - b);

  
  return parseInt(arr[0] + arr[2]) + parseInt(arr[1] + arr[3]);
};

console.log(minimumSum(4009));
