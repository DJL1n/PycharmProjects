"""
作者：legionb
日期：2024年04月08日
"""
# 每个整数可以被唯一表示为若干质数不重复的2的次幂的和
#O(b-1)->O(logb)
def q_pow(base,exponent)->int:#底数和指数
    result=1
    while exponent:
        if exponent%2==1:
            result*=base
        base*=base#实际上将已得到的数的指数左移
        exponent//=2
    return result