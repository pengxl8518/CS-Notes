from math import sqrt

'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0 or c >2**31 - 1:
            return False
        left_index = 0
        right_index = int(sqrt(c))
        while left_index <= right_index:
            if left_index**2 + right_index**2 == c:
                return True
            elif left_index**2 + right_index**2 > c:
                right_index -= 1
            else:
                left_index += 1
        return False



if __name__ == '__main__':
    engine = Solution()
    target = 1
    res = engine.judgeSquareSum(target)
    print(res)