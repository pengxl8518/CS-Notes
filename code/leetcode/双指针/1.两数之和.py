# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/21 10:16 下午
"""
代码描述：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
解题思路 空间换时间
"""


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, inputs, target):
        if not inputs:
            return None
        hashmap = {}
        for inx, val in enumerate(inputs):
            sub_val = target - val
            if sub_val in hashmap:
                return [hashmap[sub_val], inx]
            hashmap[val] = inx
        return None


if __name__ == '__main__':
    engine = Solution()
    print(engine.func([2, 7, 8, 9], 17))