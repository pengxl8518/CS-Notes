# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/25 8:28 下午
"""
代码描述：给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。
在每一天，你可能会决定购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。
返回 你能获得的 最大 利润 。
"""
from typing import List


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        profit_sum = 0
        for price in prices[1:]:
            # min_price = min(val, min_price)
            cur_profile = price - min_price
            if cur_profile > 0:
                profit_sum += cur_profile
            min_price = price
        return profit_sum


if __name__ == '__main__':
    engine = Solution()
    print(engine.func([7, 1, 5, 3, 6, 4]))