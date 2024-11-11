/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    
    while(n>4){
    let arr=n.toString().split("")
    n=0
    arr.map((el)=>{
        n+=parseInt(el)*parseInt(el)
        })
    }
    
    if(n==1) return true
    else return false
};