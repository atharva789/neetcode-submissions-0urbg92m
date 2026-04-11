class Solution:
    def isPalindrome(self, s: str) -> bool:
        # loop through with 2 pointers: moment pointer a ≠ b -> false
        alpha_numeric = []
        s = s.lower().replace(" ", "")
        i = 0
        j = len(s)-1
        while i <= len(s)-1 and j >=0:
            if s[i].isalnum() != True:
                i+=1
                continue
            if s[j].isalnum() != True:
                j-=1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -=1
        return True