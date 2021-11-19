class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        referenceList = {}
        for i in range(len(nums)):
            otherElement = target - nums[i]
            if otherElement in referenceList:
                return [referenceList[otherElement],i]
            else:
                referenceList[nums[i]]=i