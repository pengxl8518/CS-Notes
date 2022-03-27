# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/23 10:51 下午
"""
代码描述：
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；
并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/assign-cookies

贪心的思想是，用尽量小的饼干去满足小需求的孩子，所以需要进行排序先

"""
from typing import List


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_i, s_i = 0, 0
        while g_i < len(g) and s_i < len(s):
            if g[g_i] <= s[s_i]:
                g_i += 1
            s_i += 1
        return g_i


if __name__ == '__main__':
    engine = Solution()
    print(engine.func([10, 2, 3], [4, 5, 1]))