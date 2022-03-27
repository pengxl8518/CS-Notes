"""
https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E5%8F%8C%E6%8C%87%E9%92%88.md#4-%E5%9B%9E%E6%96%87%E5%AD%97%E7%AC%A6%E4%B8%B2
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        s_list = list(s)
        left_index = 0
        right_index = len(s_list)-1
        if right_index < 0 or right_index > 10**5:
            return None
        elif right_index < 2:
            return True
        else:
            while left_index < right_index:
                if s_list[left_index] != s_list[right_index]:
                    return isPalindrome(s_list, left_index+1, right_index) or isPalindrome(s_list, left_index, right_index-1)
                left_index += 1
                right_index -= 1
        return True


def isPalindrome(s_list, left_index, right_index):
    while left_index < right_index:
        if s_list[left_index] != s_list[right_index]:
            return False
        left_index += 1
        right_index -= 1
    del s_list
    return True


if __name__ == '__main__':
    engine = Solution()
    target = "abca"
    res = engine.validPalindrome(target)
    print(res)

