"""
    给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
    元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        swap = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        left_index = 0
        right_index = len(s_list)-1
        if right_index < 0 or right_index > 3 * 10**5:
            return None
        while left_index < right_index:
            if s_list[left_index] not in swap:
                left_index += 1
            else:
                if s_list[right_index] in swap:
                    swap_value = s_list[left_index]
                    s_list[left_index] = s_list[right_index]
                    s_list[right_index] = swap_value
                    right_index -= 1
                    left_index += 1
                else:
                    right_index -= 1
        return ''.join(s_list)




if __name__ == '__main__':
    engine = Solution()
    target = "coding"
    res = engine.reverseVowels(target)
    print(res)