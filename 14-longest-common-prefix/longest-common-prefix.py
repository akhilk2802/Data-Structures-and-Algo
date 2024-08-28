class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        sorted_strs = sorted(strs, key=len, reverse=True)
        prefix_string = sorted_strs[0]

        for string in sorted_strs[1:]:
            while string[:len(prefix_string)] != prefix_string:
                prefix_string = prefix_string[:-1]

                if not prefix_string:
                    return ""
        
        return prefix_string


        
        