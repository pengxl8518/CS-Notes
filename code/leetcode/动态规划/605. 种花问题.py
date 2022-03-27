# _*_coding=utf-8 _*_
# @author pxl
# @date 2022/3/25 10:20 下午
"""
代码描述：
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

防御式编程思想：在 flowerbed 数组两端各增加一个 0， 这样处理的好处在于不用考虑边界条件，任意位置处只要连续出现三个 0 就可以栽上一棵花。
"""
from typing import List


class Solution(object):
    def __init__(self):
        self.desc = 'code desc'

    def func(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        print(flowerbed)
        for i in range(1, len(flowerbed)-1):
            if (flowerbed[i-1]+flowerbed[i]+flowerbed[i+1] == 0) and n>0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0


if __name__ == '__main__':
    engine = Solution()
    print(engine.func([0,0,1,0,0], 1))