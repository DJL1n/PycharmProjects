class Graph:
    def __init__(self, adj_matrix):
    # write your codes to convert an adjacency matrix to an adjacency list
        n=len(adj_matrix)
        self.data={_:[] for _ in range(n)}
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j]==1:
                    self.data[i].append(j)

    def size(self):
        s=0
        for i in self.data.values():
            s+=len(i)
        return s
    # write your codes here

    def order(self):
        return len(self.data)
    # write your codes here

    def add_node(self, node):
        if node in self.data:
            return
        self.data[node]=[]
    # write your codes here

    def remove_node(self, node):
        if node not in self.data:
            return
        self.data.pop(node)
        for i in self.data.keys():
            if node in self.data[i]:
                self.data[i].remove(node)
    # write your codes here

    def add_arc(self, source_node, target_node):
        if target_node in self.data[source_node]:
            return
        if source_node not in self.data:
            self.add_node(source_node)
        if target_node not in self.data:
            self.add_node(target_node)
        self.data[source_node].append(target_node)
        self.data[source_node].sort()
    # write your codes here

    def remove_arc(self, source_node, target_node):
        if target_node not in self.data[source_node]:
            return
        self.data[source_node].remove(target_node)
# write your codes here.

def induced(adj_list,node_list):
    result={}
    for i in node_list:
        if i in adj_list:
            result[i]=[]
            for j in adj_list[i]:
                if j in node_list:
                    result[i].append(j)
    return result

def reverse(adj_list):
    result={_:[] for _ in adj_list.keys()}
    for i in adj_list.keys():
        for j in adj_list[i]:
            if j not in result:
                result[j]=[]
            if i not in result[j]:
                result[j].append(i)
                result[j].sort()
    return result

re = reverse({0: [1], 1: [0, 4], 2: [3, 4], 3: [2], 4: [0, 1, 2, 3]})
print(re)