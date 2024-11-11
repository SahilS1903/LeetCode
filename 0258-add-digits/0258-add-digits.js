
var addDigits = function(n) {
    while(n>9){
    let arr=n.toString().split("")
    n=0
    arr.map((el)=>{
        n+=parseInt(el)
        })
    }
    return n
};