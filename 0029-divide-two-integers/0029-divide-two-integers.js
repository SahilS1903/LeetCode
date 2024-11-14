var divide = function(dividend,divisor){
    const resIsNeg=Math.sign(divisor) !== Math.sign(dividend)
    dividend=Math.abs(dividend)
    divisor=Math.abs(divisor)

    let ret=0
    while(divisor<=dividend){
        let value=divisor
        let multiple=1
        while(value+value<=dividend){
            value+=value
            multiple+=multiple
        }
        dividend=dividend-value
        ret+=multiple
    }
    if(ret>((2**31) - 1)){
        return resIsNeg?-(2**31):(2**31)-1
    }
    return resIsNeg?-ret : ret
}