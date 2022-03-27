# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/23 11:39 下午
"""
代码描述：

"""
from typing import List

class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, price: List[int]) -> int:
        if len(price) <= 1:
            return 0
        min_price = price[0]
        max_profit = 0
        for val in price[1:]:
            min_price = min(min_price, val)
            max_profit = max(max_profit, val - min_price)
        return max_profit


if __name__ == '__main__':
    engine = Solution()
    print(engine.func([7, 1, 5, 3, 6, 4]))