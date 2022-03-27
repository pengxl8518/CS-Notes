# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/26 5:05 下午
"""
代码描述：和435类似
区别在于，[1, 2] 和 [2, 3] 在本题中算是重叠区间。
"""
from typing import List


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = 0
        nums = 1
        for inx in range(1, len(points)):
            # 如果后者的极小值 大于前者的极大值 则肯定重合了
            if points[inx-nums][1] >= points[inx][0]:
                res += 1
                # 此时面临问题是 保留谁进行下次对比
                # 贪心策略是 保留右区间更小的那个 这样才有可能获得更多的不重合解 如: 前者[4,7]和后者[5,15]
                if points[inx-nums][1] < points[inx][1]:
                    # 选择前者, 那么下一轮前者与后者间隔为num + 1
                    nums += 1
                else:
                    nums = 1
            else:
                nums = 1
        return len(points) - res


if __name__ == '__main__':
    engine = Solution()
    print(engine.func())