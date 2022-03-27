# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/26 9:32 下午
"""
代码描述：假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
贪心策略：优先排高个  高个中优先排值小的
        需要先对二维数组 做 降序+升序操作
"""
from typing import List


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]


    def func_1(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return people
        people.sort(key=lambda x: [x[0], -x[1]], reverse=True )
        for inx in range(0, len(people)):
            if people[inx][1] != inx:
                people.insert(people[inx][1], people[inx])
                del people[inx+1]
        return people


    def func_2(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return people
        people.sort(key=lambda x: [-x[0], x[1]])
        res = []
        for val in people:
            res.insert(val[1], val)
        return res


if __name__ == '__main__':
    engine = Solution()
    print(engine.func_2([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))