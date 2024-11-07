/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function (n) {
  let First = 1;
  let a = n;
  let final = 0;
  for (let i = 0; i < Math.ceil(n / 7); i++) {
    let c = First + i;

    if (a == 0) return final;

    if (a >= 7) {
      for (let j = 0; j < 7; j++) {
        final += c + j;
        a--;
      }
    } else {
      for (let j = 0; j < a; j++) {
        final += c + j;
      }
      a = 0;
    }
  }

  return final;
};

