class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str =""
        for string in strs:
            size = len(string)
            encoded_str += f"{size}#{string}"
        print(f"ENCODED_STRING: {encoded_str}")
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        while len(s) > 0:
            # parse size
            idx = 0
            size = ""
            while s[idx] != "#":
                size += s[idx]
                idx += 1
            print(f"DECODED SIZE STRING: {size}")
            size = int(size)
            string = s[idx+1:idx+size+1]
            if int(s[0]) == 0:
                string = ""
            strs.append(string)
            s = s[idx + size + 1:]
        return strs