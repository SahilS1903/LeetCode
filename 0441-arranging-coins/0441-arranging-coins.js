
var arrangeCoins = function(n) {
    let stair=0
    let i=0
    while(stair+i+1<=n){
        stair=stair+i
        if(stair+i+1<=n) i++
    }
    return i
};