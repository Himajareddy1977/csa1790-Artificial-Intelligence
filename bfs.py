graph={
    'a':['b','c','d'],
    'b':['e','f'],
    'c':['g','i'],
    'd':['i'],
    'e':[],
    'f':[],
    'g':[],
    'i':[]
}
def bfs(complete,graph,currentnode):
    complete.append(currentnode)
    queue=[]
    queue.append(currentnode)
    while queue:
        s=queue.pop(0)
        print(s)
        for neighbour in graph[s]:
            if neighbour not in complete:
                complete.append(neighbour)
                queue.append(neighbour)
bfs([],graph,"a")
