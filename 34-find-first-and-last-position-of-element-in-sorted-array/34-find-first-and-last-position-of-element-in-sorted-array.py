class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occurrence = self.findOccurrence(nums, target, first = True, last = False)
        last_occurrence = self.findOccurrence(nums, target, first = False, last = True)
        return [first_occurrence, last_occurrence]
        
    def findOccurrence(self, nums: List[int], target: int, first: bool, last: bool) -> int:
        start = 0
        end = len(nums) - 1
        occurrence = -1
        while start <= end:
            mid = start + (end - start) // 2
            if (target == nums[mid]):
                occurrence = mid
                if first:
                    end = mid - 1
                if last:
                    start = mid + 1
            elif (target < nums[mid]):
                end = mid - 1
            elif (target > nums[mid]):
                start = mid + 1
        return occurrence
                
        