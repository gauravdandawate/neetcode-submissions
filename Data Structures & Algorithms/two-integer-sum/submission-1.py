class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i,value in enumerate(nums):
            num_map[value]=i
        for i,value in enumerate(nums):
            diff=target-nums[i]
            if(diff in num_map and i != num_map[diff]):
                return [i,num_map[diff]]

