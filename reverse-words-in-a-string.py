class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        lst = []
        i, j = 0, 0
        while i+j <= len(s):
            if i + j == len(s):
                lst.append(s[i:i+j])
                lst.reverse()
                return " ".join(lst)

            if s[i] == " ":
                i += 1
            else:
                j += 1
                if s[i+j-1] == " ":
                    lst.append(s[i:i+j-1])
                    i += j
                    j = 0




s = Solution()
words = "t  "
s.reverseWords(words)

