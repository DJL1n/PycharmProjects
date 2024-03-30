class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ns = len(s) + 1
        np = len(p) + 1
        dp = [[False] * np for _ in range(ns)]
        dp[0][0] = True
        for j in range(1, np):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, ns):
            for j in range(1, np):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = (dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        return dp[ns - 1][np - 1]


