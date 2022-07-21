class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first_occurrence = occurrence(nums, target, true, false);
        int last_occurrence = occurrence(nums, target, false, true);
        int[] output = {first_occurrence, last_occurrence};
        return output;
        
    }
    public int occurrence(int[] nums, int target, boolean first, boolean last) {
        int start = 0;
        int end = nums.length - 1;
        int position = -1;
        while(start <= end) {
            int mid = start + (end - start) / 2;
            if (target == nums[mid]) {
                position = mid;
                if (first) {
                    end = mid - 1;
                }
                if (last) {
                    start = mid + 1;
                }
            }
            else if (target < nums[mid]) {
                end = mid - 1;
            }
            else if (target > nums[mid]) {
                start = mid + 1;
            }
        }
        return position;
    }
}