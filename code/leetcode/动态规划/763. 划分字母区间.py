# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/26 10:08 下午
"""
代码描述：字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
链接：https://leetcode-cn.com/problems/partition-labels/

"""
from typing import List


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, s):
        start, end = 0, 0
        res = []
        dict_s = {}
        for inx in range(0, len(s)):
            dict_s[s[inx]] = inx
        for inx in range(0, len(s)):
            end = max(end, dict_s[s[inx]])
            if inx == end:
                res.append(end-start+1)
                start = inx + 1
        return res


if __name__ == '__main__':
    engine = Solution()
    S = "ababcbacadefegdehijhklij"
    print(engine.func(S))