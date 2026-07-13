class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length;
        int left=-1;
        int right=-1;
        int i=1;
        int j=n-2;
        int max=nums[0];
        while(i<=n-1){
            max=Math.max(nums[i],max);
            if(nums[i]<max){
                right=i;
            }
            i++;
        }
        int min=nums[n-1];
        while(j>=0){
            min=Math.min(nums[j],min);
            if(nums[j]>min){
                left =j;
            }
            j--;
        }
        if(left==-1 && right==-1){
            return 0;
        }else{
            return right-left+1;
        }
    }
}