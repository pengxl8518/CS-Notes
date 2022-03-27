from typing import List

"""
给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(nums)-1
        if right_index <= 0:
             return None
        while left_index < right_index:
            if nums[left_index] + nums[right_index] == target:
                return [left_index+1, right_index+1]
            elif nums[left_index] + nums[right_index] > target:
                right_index -= 1
            else:
                left_index += 1


if __name__ == '__main__':
    engine = Solution()
    nums = [2,7,11,15]
    target = 22
    res = engine.twoSum(nums, target)
    print(res)
