# 12-05-2025

# 2094  finding 3-digit even numbers



# Input: digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]
# Explanation: All the possible integers that follow the requirements are in the output array. 
# Notice that there are no odd integers or integers with leading zeros.

# code 

from collections import Counter

def findEvenNumbers(digits):
        
        freq = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            parts = [num // 100, (num // 10) % 10, num % 10]
            count = Counter(parts)
            if all(freq[d] >= count[d] for d in count):
                res.append(num)
        return res
        
print(findEvenNumbers([2,1,3,0]))




# 13-05-2025 

#3335 - total characters in string after transformations I

# Input: s = "abcyy", t = 2

# Output: 7

# Explanation:

# First Transformation (t = 1):
# 'a' becomes 'b'
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'y' becomes 'z'
# 'y' becomes 'z'
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'd' becomes 'e'
# 'z' becomes "ab"
# 'z' becomes "ab"
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.


 # code --------------------------------------

 class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        nums = [0]*26
        for ch in s:
            nums[ord(ch) - 97] += 1

        for _ in range(t):
            cur = [0]*26
            z = nums[25]
            if z:
                # 'z' → 'a' and 'b'
                cur[0] = (cur[0] + z) % mod
                cur[1] = (cur[1] + z) % mod
            for j in range(25):
                v = nums[j]
                if v:
                    cur[j+1] = (cur[j+1] + v) % mod
            nums = cur

        res = 0
        for v in nums:
            res = (res + v) % mod
        return res


# 14-05-2025


# learnt the sliding problem approaches and solve the problems using the fixed sliding window
        
