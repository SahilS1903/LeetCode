
function subsetXORSum(nums) {
    let totalXorSum = 0;
    const n = nums.length;

    
    for (let i = 0; i < (1 << n); i++) {
        let xorTotal = 0;
        for (let j = 0; j < n; j++) {
            
            if (i & (1 << j)) {
                xorTotal ^= nums[j];
            }
        }
        totalXorSum += xorTotal;
    }

    return totalXorSum;
}

