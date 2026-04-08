class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashtable_s, hashtable_t = {}, {}
        for char in s:
            if char not in hashtable_s:
                hashtable_s[char] = 1
                continue
            hashtable_s[char] += 1
        for char in t:
            if char not in hashtable_t:
                hashtable_t[char] = 1
                continue
            hashtable_t[char] += 1
        for key_s in hashtable_s.keys():
            if key_s not in hashtable_t:
                return False
            if hashtable_s[key_s] != hashtable_t[key_s]:
                return False
        return True

            