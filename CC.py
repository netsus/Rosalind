# coding: utf-8
"""
난이도 : 3.3

문제 : 첫 줄에 정점 수(v)와 연결선 수(e)를 주고, 다음줄 부터 서로 연결된 두 정점을 행 구분자로 입력해 준다.
    1번 부터, v까지 정점이 있을 때, 연결선으로 연결된 연결 요소들이 모두 몇개인지 출력. (연결선 없이 정점 1개만 있는것 도 연결 요소 1개로 친다.)

알고리즘 : Make_Graph함수에서 graph에 그래프를 만든다. 두 정점으로 1 2 가 주어졌다고 할 때, graph는 {1:[2] , 2:[1]} 이렇게 양 방향으로 정점과 연결된 정점을 추가해준다.
    (양 방향으로 하는 이유는 연결 요소를 DFS로 탐색할때 어떤 정점에서 탐색해도 탐색이 가능하게 하기 위함이다.)
    또한 정점 집합합
    이후에, 1번 부터, v까지 반복하며 정점 집합 s를 만들어 준다. -> 나중에 연결요소가 생성 될때마다 s에서 연결 요소를 제거하며 Count 하기 위함이다.

    count_CC함수에서 s에 원소가 남아있는 동안 반복하며,
        방문한 정점 집합임 visited에 대해, s에 첫번째 원소를 첫 방문 정점(first)으로 하여 dfs를 실행한다.
        dfs가 에러나는 경우는 연결 선 없이 정점 1개만 있는 경우이므로.
        이런 경우는 except에서서 visited에 해당 정점 first를 넣어주고 s = s- visitied에서 제외하는 방식으로 진행한다.
        s에서 방문한 정점들(visited)가 제외 되면, 연결 요소(cc)가 1 증가하며, 연결요소 개수를 센다.

    dfs는 깊이 우선 탐색으로, 그래프(graph)에서 주어진 정점(first)에 대해 더 이상 다음 노드가 나오지 않을 때 까지 연결된 다음 노드를 방문한다.
    더 이상 다음 노드가 나오지 않게 되면, dfs 내부의 for 문이 종료되며 백트래킹이 일어난다.
    여기서 백트래킹이란 퇴각 검색법으로,
    dfs 함수가 꼬리에 꼬리를 물고 계속 실행 되는데, dfs의 for 문이 종료되면, 그 전에 실행 되었던 dfs의 for문이 실행되는 방식을 말한다.
    ex) dfs 호출 순서에따라 번호를 붙였을때,
    dfs1 -> dfs2 -> dfs3 -> dfs4 
    에서 dfs4의 for문이 종료되면,
    dfs3 for문으로 돌아가가 다음 neighbour를 반복하게되는 것을 말한다.

"""

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def Make_Graph(f):
    graph={};s=set()
    v,e = map(int,f.readline().strip().split())

    for line in f:
        start,end = map(int,line.split())
        if start not in graph.keys():
            graph[start]=[]
            graph[start].append(end)
        else:
            graph[start].append(end)
        if end not in graph.keys():
            graph[end]=[]
            graph[end].append(start)
        else:
            graph[end].append(start)

    for i in range(1,v+1):
        s.add(i)
    return graph,s

def count_CC(graph,s):
    cc=0
    while s:
        visited = set()
        first = list(s)[0]
        try:
            dfs(visited,graph,first)
        except:
            visited.add(first)
        s = s - visited
        cc+=1
    return cc

with open('../dataset/rosalind_cc.txt') as f:
    graph,s = Make_Graph(f)
    cc = count_CC(graph,s)
    print(cc)