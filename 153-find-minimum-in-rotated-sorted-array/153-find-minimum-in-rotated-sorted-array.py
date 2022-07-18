class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l = 0
        # r = len(nums) - 1
        # res = nums[0]
        # while l <= r:
        #     if nums[l] < nums[r]:
        #         res = min(res, nums[l])
        #         break
        #     mid = (l+r) // 2
        #     res = min(res, nums[mid])
        #     if nums[mid] >= nums[l]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return res
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            next_item = (mid + 1) % len(nums)
            prev_item = (mid + len(nums) - 1) % len(nums)
            if (nums[mid] <= nums[next_item] and nums[mid] <= nums[prev_item]):
                return nums[mid]
            elif (nums[mid] >= nums[start] and nums[mid] <= nums[end]):
                return nums[start]
            elif (nums[start] <= nums[mid]):
                start = mid + 1
            elif (nums[mid] <= nums[end]):
                end = mid - 1
        
        
        
        
        