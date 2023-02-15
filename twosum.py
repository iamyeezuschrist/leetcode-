class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = dict()

        for i in range(len(nums)):
            left = target - nums[i]

            if left in dictionary.keys():
                return dictionary[left], i

            dictionary[nums[i]] = i

