class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            int next_item = (mid +1) % nums.length;
            int prev_item = (mid + nums.length -1) % nums.length;
            if (nums[mid] <= nums[next_item] && nums[mid] <= nums[prev_item]) {
                return nums[mid];
            }
            else if (nums[start] <= nums[mid] && nums[mid] <= nums[end]) {
                return nums[start];
            }
            else if(nums[start] <= nums[mid]) {
                start = mid + 1;
            }
            else if(nums[mid] <= nums[end]) {
                end = mid - 1;
            }
        }
        return -1;
    }
}