# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/26 4:32 下午
"""
代码描述：
给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
"""
from typing import List


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        nums = 1
        for inx in range(1, len(intervals)):
            # 如果后者的极小值 大于前者的极大值 则肯定重合了
            if intervals[inx-nums][1] > intervals[inx][0]:
                res += 1
                # 此时面临问题是 保留谁进行下次对比
                # 贪心策略是 保留右区间更小的那个 这样才有可能获得更多的不重合解 如: 前者[4,7]和后者[5,15]
                if intervals[inx-nums][1] < intervals[inx][1]:
                    # 选择前者, 那么下一轮前者与后者间隔为num + 1
                    nums += 1
                else:
                    nums = 1
            else:
                nums = 1
        return res


if __name__ == '__main__':
    engine = Solution()
    print(engine.func([[0,2],[1,3],[2,4],[3,5],[4,6]]))