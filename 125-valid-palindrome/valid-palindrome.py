class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        cs = cleaned_string.lower()
        start = 0
        end = len(cs)-1

        while start < end:
            if cs[start] == cs[end]:
                start += 1
                end -= 1
            else:
                return False

        return True