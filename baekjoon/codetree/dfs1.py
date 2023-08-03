# https://www.codetree.ai/missions/2/problems/graph-traversal/introduction

import sys

N, M = map(int, input().split())
graph = {}
for i in range(N):
    graph[i+1] = []
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

need_visit = graph[1]
visited = set()
visited.add(1)

while len(need_visit) != 0:
    if need_visit[0] in visited:
        need_visit.pop(0)
    else:
        visited.add(need_visit[0])
        need_visit.extend(graph[need_visit[0]])
        need_visit.pop(0)


print(len(visited)-1)