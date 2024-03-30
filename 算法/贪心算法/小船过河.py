"""
作者：legionb
日期：2024年03月16日
"""
people=list(map(int,input().split()))
n=len(people)
sort_peo=sorted(people)
time=sort_peo[0]*2*n+sum(sort_peo[1:])