class Graph:
    '''
    using list of neighbors
    format is like that:
    [node,connected1,connected2,...]
    '''
    def __init__(self):
        self.graph = []
    def addNode(self,val):
        self.graph.append([val]) #O(V)
    def addEdge(self,node1,node2):#O(V+E)
        for i in self.graph:
            if i[0] == node1:
                i.append(node2)
            if i[0] == node2:
                i.append(node1)
    def neighboors(self,node):
        for i in self.graph:
            if i[0] == node:
                return i[1:]
    def DFSUTIL(self,end,node,visited,way):
        visited.append(node)
        way.append(node)
        if node == end:
            return way
        for i in self.neighboors(node):
            if not i in visited:
                x = self.DFSUTIL(end,i,visited,way) 
                if x != None:
                    return x
        way.pop()
        return None
    def DFS(self,start,end):
        return self.DFSUTIL(end,start,[],[])
def neighboors(x):
    return [(x[0],x[1]-1),(x[0]-1,x[1]),(x[0]+1,x[1]),(x[0],x[1]+1)]

f = open("maze.txt","r")
s = f.read().splitlines()
f.close()
frees = []
start,end = None,None
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] == '0':
            frees.append((i,j))
        if s[i][j] == 's':
            start = (i,j)
        if s[i][j] == 'e':
            end = (i,j)
frees.append(start)
frees.append(end)
#print(start)
#print(end)
#print(*frees)
graph = Graph()
for i in frees:
    graph.addNode(i)
for x in range(len(frees)):
    for y in range(x,len(frees)):
        i,j = frees[x],frees[y]
        if j in neighboors(i):
            graph.addEdge(i,j)
way = graph.DFS(start,end)
for i in range(len(s)):
    s[i] = list(s[i])

for i in range(len(s)):
    for j in range(len(s[i])):
        if (i,j) in way:
            s[i][j] = 'x'
st = ''
for i in s:
    for j in i:
        st+=j
    st+='\n'
#print(*graph.graph)
f = open("solved.txt",'w')
f.write(st)