from collections import defaultdict

def dfs(graph, start, end, visited=[], path=[]):
    visited = visited + [start]
    if start == end:
        path.append(visited)

    for node in graph[start]:
        if node not in visited:
            dfs(graph,node,end,visited, path)

    return len(path)

            
def solution(depar, hub, dest, roads):
    d = defaultdict(list)
    for i,j in roads:
        d[i].append(j)

    return (dfs(d, depar, hub, [], []) * dfs(d, hub, dest, [], [])) % 10007





depar = "SEOUL"
depar = "ULSAN"
hub = "DAEGU"
hub = "SEOUL"
dest = "YEOSU"
dest = "BUSAN"
roads = [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]
roads = [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]

print(solution(depar, hub, dest, roads))


