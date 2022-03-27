# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/26 3:49 下午
"""
代码描述：
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。

贪心思想： 只要当前累计值不小于零 则一直往后累加，当每次累计时 最大值为 前一累加最大值 和当前累加最大值
max_sum 需要初始化为 负无穷

"""
from typing import List


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, nums: List[int]) -> int:
        if not nums:
            return None
        max_sum, cur_sum = float('-inf'), 0
        for val in nums:
            cur_sum += val
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum


if __name__ == '__main__':
    engine = Solution()
    print(engine.func([-2, 1, -3, 4, -1, 2, 1, -5, 4]))