# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/25 10:44 下午
"""
代码描述：
给你一个长度为 n 的整数数组 nums ，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-decreasing-array
贪心策略：
    只要当前值小于前一值，则将前一位置的值 置换为当当前值
    特殊情况：
        当前值 小于前一位置值及 inx-2上的值，此时 需要替换当前位置的值 为 inx-1上的值
"""
from typing import List


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        cnt = 0
        inx = 1
        while inx < len(nums) and cnt <= 1:
            if nums[inx-1] <= nums[inx]:
                inx += 1
                continue
            cnt += 1
            # 特殊情况，当前值比前面两个数都小，此时，修改将inx上的值 置换为inx-1上的值
            if inx-2 >= 0 and nums[inx-2] > nums[inx]:
                nums[inx] = nums[inx-1]
            # 当前值比之前的值小，此时 修改inx-1上的值 并将重置为当前值
            else:
                nums[inx-1] = nums[inx]
            inx += 1
        return cnt <= 1


if __name__ == '__main__':
    engine = Solution()
    print(engine.func([2, 2, 3, 3, 2, 4]))