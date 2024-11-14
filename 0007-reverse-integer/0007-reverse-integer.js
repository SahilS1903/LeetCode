/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let sign=1 // 1 is +ve

    if(x<0){
        sign=0
        x*=-1
    }
    x=parseInt(x.toString().split("").reverse().join(""))
    
    if(-2147483648 <= x && x <= 2147483647){
    if(sign==0) return -1*x
    else return x
    }return 0

};
