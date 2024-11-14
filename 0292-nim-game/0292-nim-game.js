/**
 * @param {number} n
 * @return {boolean}
 */
var canWinNim = function(n) {
    return (n==1 || n==2 || n==3 || (n%2==1 || (n-2)%4==0)) 
};