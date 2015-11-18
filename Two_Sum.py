class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        bak = nums[:]
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            if (nums[left] + nums[right]) == target:
                break
            elif (nums[left] + nums[right]) > target:
                right -= 1
            else:
                left += 1

        answer = []

        for i, item in enumerate(bak):
            if item == nums[left] or item == nums[right]:
                answer.append(i+1)
        return answer

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for i in xrange(len(nums)):
            x = nums[i]
            if target - x in my_dict.keys():
                return my_dict[target - x] + 1, i + 1
            else:
                my_dict[x] = i