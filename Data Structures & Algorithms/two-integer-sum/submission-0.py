class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tar = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in tar:
                return [tar[diff],i]
            tar[num]=i

