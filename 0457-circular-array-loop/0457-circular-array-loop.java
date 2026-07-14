class Solution {
    public boolean circularArrayLoop(int[] nums) {
        for(int i=0;i<nums.length;i++){
            int slow=i;
            int fast=i;
            if(nums[i]>0){
                do{
                    slow = ((slow + nums[slow]) % nums.length + nums.length) % nums.length;
                    fast = ((fast + nums[fast]) % nums.length + nums.length) % nums.length;
                    if(nums[fast]<0) break;
                    fast = ((fast + nums[fast]) % nums.length + nums.length) % nums.length;
                    if(nums[fast]<0) break;
                }while(slow!=fast);
                if(slow==fast && nums[fast]>0){
                int temp=slow;
                temp = ((temp + nums[temp]) % nums.length + nums.length) % nums.length;
                if(slow==temp) continue;
                else return true;
            }
            }else{
                do{
                    slow = ((slow + nums[slow]) % nums.length + nums.length) % nums.length;
                    fast = ((fast + nums[fast]) % nums.length + nums.length) % nums.length;
                    if(nums[fast]>0) break;
                    fast = ((fast + nums[fast]) % nums.length + nums.length) % nums.length;
                    if(nums[fast]>0) break;
                }while(slow!=fast);
                if(slow==fast && nums[fast]<0){
                int temp=slow;
                temp = ((temp + nums[temp]) % nums.length + nums.length) % nums.length;
                if(slow==temp) continue;
                else return true;
            }
            }
            
        }
        return false;
    }
}