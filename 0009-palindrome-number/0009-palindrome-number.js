/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let n=x.toString();
    let m=n.length;
    for(let i=0;i<Math.floor(m/2);i++){
        if(n.charAt(i)!=n.charAt(m-i-1)) return false
    }
    return true
};