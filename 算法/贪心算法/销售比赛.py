"""
作者：legionb
日期：2024年03月23日
"""
import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    res = 0
    q = []

    res -= price[0]
    res += price[-1]

    for i in range(1, n - 1, 2):
        buy = min(price[i], price[i + 1])
        sell = max(price[i], price[i + 1])

        if q:
            if buy > q[0]:
                res = res - 2 * heapq.heappop(q) + buy + sell
                heapq.heappush(q, buy)
                heapq.heappush(q, sell)
            else:
                res = res - buy + sell
                heapq.heappush(q, sell)
        else:
            res = res - buy + sell
            heapq.heappush(q, sell)

    print(res)
