class Solution {
    public int totalFruit(int[] nums) {
        int i=0;
        int j=0;
        int max=-1;
        Map<Integer,Integer> freq=new HashMap<>();
        while(j<nums.length){
            freq.put(nums[j],freq.getOrDefault(nums[j],0)+1);
            while(freq.size()>2){
                int left=nums[i];
                freq.put(left,freq.get(left)-1);
                if (freq.get(left) == 0) freq.remove(left);
                i++;
            }
            if(freq.size()<=2){
                max=Math.max(max,j-i+1);
            }
            j++;
        }
        return max;
    }
}