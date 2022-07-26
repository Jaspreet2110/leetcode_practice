class Solution {
    public int search(int[] nums, int target) {
        int minIndex = minElementIndex(nums);
        int firstHalf = binarySearch(nums, 0, minIndex-1, target);
        int secondHalf = binarySearch(nums, minIndex, nums.length-1, target);
        if (firstHalf != -1) {
            return firstHalf;
        }
        else if (secondHalf != -1){
            return secondHalf;
        }
        return -1;
        
    }
    public int minElementIndex(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            int nextElement = (mid + 1) % nums.length;
            int prevElement = (mid + nums.length - 1) % nums.length;
            if (nums[start] <= nums[mid] && nums[mid] <= nums[end]) {
                return start;
            }
            else if (nums[mid] <= nums[nextElement] && nums[mid] <= nums[prevElement]){
                return mid;
            }
            else if (nums[start] <= nums[mid]){
                start = mid + 1;
            }
            else if(nums[mid] <= nums[end]) {
                end = mid - 1;
            }
        }
        return -1;
    }
    public int binarySearch(int[] nums, int start, int end, int target) {
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (target == nums[mid]) {
                return mid;
            }
            else if (target < nums[mid]) {
                end = mid - 1;
            }
            else if (target > nums[mid]) {
                start = mid + 1;
            }
        }
        return -1;
    }
}