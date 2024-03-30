class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = [[None]]
        result.append(['()'])
        for i in range(2, n + 1):
            lst = []
            for j in range(i):
                past1 = result[j]
                past2 = result[i - 1 - j]
                for k1 in past1:
                    for k2 in past2:
                        if k1 == None:
                            k1 = ''
                        if k2 == None:
                            k2 = ''
                        new = '(' + k1 + ')' + k2
                        lst.append(new)
            result.append(lst)
        return result[n]

