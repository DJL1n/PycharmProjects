"""
作者：legionb
日期：2024年04月07日
"""


def runnian(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


count = 0
short = [4, 6, 9, 11]
for i in range(1900, 9999):
    year = i
    left = year // 100 // 10 + year // 100 % 10 + year % 100 // 10 + year % 100 % 10
    for j in range(1, 13):
        for k in range(1, 32):

            month, day = j, k

            right = month // 10 + month % 10 + day // 10 + day % 10
            if left == right:
                count += 1
                print(i,j,k)
            if not runnian(i) and j == 2 and k == 28:
                break
            elif j == 2 and k == 29:
                break
            elif j in short and k == 30:
                break
print(count)
