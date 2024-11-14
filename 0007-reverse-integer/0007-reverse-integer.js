/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
     

    
    let rev=parseInt(x.toString().split("").reverse().join(""))
    
    if(-2147483648 <= rev && rev <= 2147483647){
    if(x<0) return -(rev)
    else return rev
    }return 0

};
