import sys


def first_judge(lst):
    for i in range(n):
        if i % 2 == 1 and lst[i] % 2 == 1 or i % 2 == 0 and lst[i] % 2 == 0:
            return False
    return True


def second_judge():
    dp = [[0] * n for _ in range(3)]
    for start in range(0, n - 1):
        dp[0][start] = num[start] + num[start + 1]
        if dp[0][start] > m: return False
    for start in range(0, n - 2):
        dp[1][start] = dp[0][start] + num[start + 2]
        if dp[1][start] > m: return False
    for start in range(0, n - 4):
        dp[2][start] = dp[1][start] + dp[0][start + 3]
        if dp[2][start] > m: return False
    print(dp)
    return True


sys.set_int_max_str_digits(200001)
n, m = map(int, input().split())
count = 0
for i in range(10 ** (n - 1), 10 ** n):
    num = [int(_) for _ in str(i)]
    num = num[::-1]
    print(i)
    if not first_judge(num):
        continue
    if second_judge():
        count += 1
print(count % 998244353)

# 大佬写法
M, mod, ans, p, q = 12, 998244353, 0, 1, 0
n, m = map(int, input().split())
g = [[[[[0 for _ in range(M)] for _ in range(M)] for _ in range(M)] for _ in range(M)] for _ in range(2)]
for a in range(p, 10, 2):  # 维护二维的前缀和？ 预处理出前4位的情况
    for b in range(q, 10, 2):
        for c in range(p, 10, 2):
            for d in range(q, 10, 2):
                g[0][a + 2][b][c][d] = g[0][a][b][c][d] + int(a + b + c + d <= m)
for i in range(5, n + 1):  # 从第五位开始
    p, q = p ^ 1, q ^ 1
    for a in range(p, 10, 2):
        for b in range(q, 10, 2):
            for c in range(p, 10, 2):
                for d in range(q, 10, 2):
                    f = m - a - b - c - d  # 计算f值
                    if q != (f & 1): f -= 1  # 余数f与当前位置的奇偶性不同则f--   q表示奇偶情况
                    if f > 8 + p: f = 8 + q  # 控制余数f在0~9范围内
                    g[i % 2][a + 2][b][c][d] = (g[i % 2][a][b][c][d] + (
                        0 if f < q else g[(i + 1) % 2][f + 2][a][b][c])) % mod
for b in range(q, 10, 2):
    for c in range(p, 10, 2):
        for d in range(q, 10, 2):
            f = m - b - c - d
            if f < p: continue
            if p != (f & 1): f -= 1
            if f > 8 + p: f = 8 + p
            ans = (ans + g[n % 2][f + 2][b][c][d]) % mod
print(ans)
