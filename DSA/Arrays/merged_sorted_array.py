class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = m - 1
        l = n - 1
        k = m + n - 1

        while j >= 0 and l >= 0 :
            if nums1[j] > nums2[l]:
                nums1[k] = nums1[j]
                j -= 1
            else:
                nums1[k] = nums2[l]
                l -= 1
            k -= 1

        while l >= 0:
            nums1[k] = nums2[l]
            l -= 1
            k -= 1
  
        