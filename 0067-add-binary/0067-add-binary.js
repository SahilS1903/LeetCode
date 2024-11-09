/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let length;
    let carry = 0;
    let ans = "";

    
    if (a.length > b.length) {
        length = a.length;
        b = b.padStart(length, "0");
    } else {
        length = b.length;
        a = a.padStart(length, "0");
    }

    for (let i = length - 1; i >= 0; i--) {
        
        const bitA = parseInt(a.charAt(i), 10);
        const bitB = parseInt(b.charAt(i), 10);

        
        const sum = bitA + bitB + carry;
        ans = (sum % 2) + ans;
        carry = Math.floor(sum / 2); 
    }

   
    if (carry === 1) {
        ans = "1" + ans;
    }

    return ans;
};
