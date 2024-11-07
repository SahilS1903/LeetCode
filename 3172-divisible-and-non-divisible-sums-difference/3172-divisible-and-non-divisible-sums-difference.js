
var differenceOfSums = function(n, m) {
    let num1=0;
    let num2=0;
    for(i=1;i<=n;i++){
        i%m!=0 ? num1+=i: num2+=i
    }
    return num1-num2
};