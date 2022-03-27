from typing import List
"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：
双指针
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_index = m-1
        right_index = n-1
        all_len = m+n-1
        while right_index >= 0:
            if nums1[left_index] > nums2[right_index] and left_index>=0:
                nums1[all_len] = nums1[left_index]
                left_index -= 1
                all_len -= 1
            else:
                nums1[all_len] = nums2[right_index]
                right_index -= 1
                all_len -= 1
        return nums1


if __name__ == '__main__':
    engine = Solution()
    nums1 = [1, 2, 7, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    res = engine.merge(nums1, m, nums2, n)
    print(res)
