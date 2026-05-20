class Solution {
    public void sortColors(int[] nums) {
        int i=0;
        int j=0;
        int k=nums.length-1;
        while(i<=k){
            if(nums[i]==0){
                if(i==j){
                    i++;
                    j++;
                }
                else{
                    nums[j]=0;
                    j++;
                    nums[i]=1;
                    i++;
                }
            }
            else if(nums[i]==2){
                nums[i]=nums[k];
                nums[k]=2;
                k--;
            }else i++;
           
        }
    }
}