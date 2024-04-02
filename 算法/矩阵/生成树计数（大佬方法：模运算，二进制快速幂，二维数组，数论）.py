mod = int(1e9) + 7
def fpow(a, b):
    res = 1
    while b:
        if b & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b >>= 1
    return res
n, m = map(int, input().split())
buffer = [input() for _ in range(n)]
p = [[0] * 100005 for _ in range(6)]
s = 0
for j in range(m):
    for i in range(n):
        p[i][j] = s + 1 if buffer[i][j] == 'E' else 0
        if p[i][j]:
            s += 1
map = [[0] * 13 for _ in range(600030)]
for i in range(n):
    for j in range(m):
        if p[i][j]:
            if i-1 >= 0 and p[i-1][j]:
                map[p[i][j]-1][6] += 1
                map[p[i][j]-1][6-p[i][j]+p[i-1][j]] -= 1
            if i+1 < n and p[i+1][j]:
                map[p[i][j]-1][6] += 1
                map[p[i][j]-1][6-p[i][j]+p[i+1][j]] -= 1
            if j-1 >= 0 and p[i][j-1]:
                map[p[i][j]-1][6] += 1
                map[p[i][j]-1][6-p[i][j]+p[i][j-1]] -= 1
            if j+1 < m and p[i][j+1]:
                map[p[i][j]-1][6] += 1
                map[p[i][j]-1][6-p[i][j]+p[i][j+1]] -= 1
res = 1
for i in range(s - 1):
    res = (res * map[i][6]) % mod
    for j in range(1, min(6, s-1-i)+1):
        if map[i+j][6-j] != 0:
            scale = (map[i+j][6-j] * pow(map[i][6], mod - 2, mod)) % mod
            for k in range(6, 13):
                map[i+j][k-j] = (map[i+j][k-j] - map[i][k] * scale) % mod
print(res)
#运用了模运算、二进制快速幂、二维数组操作、以及递推关系和数论知识