/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let a=1;
    let b=2;
    if (n==1 || n==2) return n
    let c
    
    for(let i=2;i<n;i++){
        c=a+b;
        a=b;
        b=c;
    }
    return b

};