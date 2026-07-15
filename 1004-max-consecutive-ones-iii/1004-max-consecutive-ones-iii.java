class Solution {
    public int longestOnes(int[] nums, int k) {
        int[] count={0,0};
        int i=0;
        int max=0;
        for(int j=0;j<nums.length;j++){
            count[nums[j]]+=1;
            while(count[0]>k){
                int left=nums[i];
                count[left]-=1;
                i++;
            }
            if(j-i+1-count[1]<=k){
                max=Math.max(max,j-i+1);
            }
        }
        return max;
    }
}