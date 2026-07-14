class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int min=Integer.MAX_VALUE;

        //BRUTE FORCE SOLUTION

        // for(int i=0;i<nums.length;i++){
        //     int sum=0;
            
        //     for(int j=i;j<nums.length;j++){
                
        //         sum+=nums[j];
        //         System.out.println(sum);
        //         if(sum>=target){
        //             min=Math.min(min,j-i+1);
        //             break;

        //         }
        //     }
        // }

        int i=0;
        int j=0;
        int sum=0;
        while(j<nums.length){
            sum+=nums[j];
            while(sum>=target){
                min=Math.min(min,j-i+1);
                sum-=nums[i];
                i++;
            }
            j++;
        }

        return min==Integer.MAX_VALUE?0:min;
    }
}