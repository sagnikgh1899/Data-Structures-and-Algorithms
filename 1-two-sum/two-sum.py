from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = defaultdict()
        for i in range(len(nums)):
            if (target - nums[i]) in Dict:
                return [Dict[target - nums[i]], i]
            else:
                Dict[nums[i]] = i
        return []
        