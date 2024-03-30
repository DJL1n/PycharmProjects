class Hash:
    def __init__(self,size=11):
        self.hash_table=[None]*size
        self.size=size
#线性搜索
    def hash(self,target,i=0):
        #包括搜索目标和寻找空位
        h_value=(target+i)%self.size
        if self.hash_table[h_value]==target:
            return h_value
        if self.hash_table[h_value] is not None:
            i+=1
            h_value=self.hash(target,i)
        return h_value
    def put(self,k):
        index=self.hash(k,0)
        self.hash_table[index]=k
    def get(self,k):
        return self.hash_table[self.hash(k,0)]

#引入载荷因子的概念，=已有元素个数/表长
class Map:
    def __init__(self,size=11):
        self.capacity=size
        self.hash_table=[None]*size
        self.num=0
        self.load_factor=0.75
    def hash(self,target,i=0):
        h_value = (target + i) % self.size
        if self.hash_table[h_value] == target:
            return h_value
        if self.hash_table[h_value] is not None:
            i += 1
            h_value = self.hash(target, i)
        return h_value
    def resize(self):
        #扩容到原有元素数量的两倍
        self.capacity=self.num*2
        temp=self.hash_table[:]
        self.hash_table=[None]*self.capacity
        for i in temp:
            if i is not None:
                hash_v=