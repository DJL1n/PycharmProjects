class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if s[i - 1] == '(':
                dp[i] = 0
            else:
                if i - 2 >= 0 and s[i - 2] == '(':
                    dp[i] = 2 + dp[i - 2]
                else:
                    if i - 2 >= 1 and i - 2 - dp[i - 1] >= 0 and s[i - 2 - dp[i - 1]] == '(':
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        dp[i] = 0
        return max(dp)

