from typing import List

'''
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longestWord = ''
        for target in dictionary:
            if len(longestWord) > len(target) or (len(longestWord) == len(target) and longestWord < target):
                continue
            else:
                if self.isSubstr(s, target):
                    longestWord = target
        return longestWord


    def isSubstr(self, s, target):
        s_index, target_index = 0, 0
        while s_index < len(s) and target_index < len(target):
            if s[s_index] == target[target_index]:
                target_index += 1
            s_index += 1
        return target_index == len(target)


if __name__ == '__main__':
    engine = Solution()
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    res = engine.findLongestWord(s, dictionary)
    print(res)