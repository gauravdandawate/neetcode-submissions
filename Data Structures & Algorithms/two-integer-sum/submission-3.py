class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}

        for i,value in enumerate(nums):
            diff=target-value
            if(diff in num_map):
                return [num_map[diff],i]
            num_map[value]=i

