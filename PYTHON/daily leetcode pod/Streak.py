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