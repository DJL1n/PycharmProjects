"""
作者：legionb
日期：2024年03月13日
"""
def greedy_activity_selector(activities):
    num = 1
    i = 1
    for j in range(2,len(activities)):
        if activities[j]['start']>=activities[i]['start']:
            i=j
            num+=1
    return num


t=int(input())
for i in range(t):
    N=int(input())
    activities=[]
    for j in range(N):
        start,end=map(int,input().split())
        activities.append({'start':start,'end':end})
    activities.sort(key=lambda x:x['end'])
    res=greedy_activity_selector(activities)
    print(res)