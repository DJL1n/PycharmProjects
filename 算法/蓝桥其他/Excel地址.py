"""
作者：legionb
日期：2024年04月02日
"""
def trans(n,str1):
    print(n)
    if n<=26:
        # if n==0:
        #     return 'Z'+str1
        return chr(64+n)+str1
    a=n%26
    b=n//26
    print(b)
    if a==0:
        b-=1
        a=26
    str1=chr(64+a)+str1
    return trans(b,str1)
print(trans(int(input()),""))
#麻烦点在于整除时要借位达到目的
#之前有地方理解不对，26是Z，AZ记录的是第二个AZ