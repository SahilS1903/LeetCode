
var minimumOperations = function(nums) {
    let num=0
    nums.map((x)=>{
        if(x%3!=0) num+=1;  
    })
    return num
};