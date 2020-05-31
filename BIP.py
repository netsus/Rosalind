# coding: utf-8
"""
난이도 : 5

문제 : 정수(k) - 그래프 개수가 주어지고,
    한 줄씩 띄워서, 각 그래프에 대한 정보가 주어진다.
    그래프에 대한 정보는 첫줄에 v(정점 개수), e(간선 개수)가 주어지고,
    둘째줄 부터, 서로 연결된 두 정점(정점1 정점2)이 정점수(v)만큼 주어진다. (그래프가 여러개 일때 한 행씩 띄워서 다음 그래프에 대한 정보가 주어짐)
    -> 출력은 각 그래프가 이분그래프(Bipartite graph) 이면 1을 출력하고, 이분그래프가 아니면 -1 출력.

    * 이분그래프: 그래프의 모든 정점이 두 그룹으로 나눠지고 서로 다른 그룹의 정점이 간선으로 연결되어져 있는(<=> 같은 그룹에 속한 정점끼리는 서로 인접하지 않도록 하는) 그래프.

알고리즘 : 주요 흐름은, 그래프의 시작점(visited[1]번) 부터 DFS(깊이우선탐색)을 하면서 각 정점에 대해 group을 준다.(group 정보는 visited 리스트에 저장)
즉, 처음 방문한 정점엔 group을 1로주고, 다음 방문한 정점엔 group을 -1로 주고, 또 다음 정점엔 1 주면서 DFS를 진행한다.
    모든 정점에 대해 DFS가 진행되며 group이 1, -1, 1, -1 순차적으로 잘 되면, bipartite 함수내에서 dfs 함수의 최종 return은 True가 되어 결과 적으로 1이 출력된다.(이분그래프가 맞다는 의미.)
    DFS 진행시 group으로 1, -1, 1, -1 을 주는데 1 뒤에 1이 나오거나, -1 뒤에 -1이 나오게 되면 line51에서 False가 나오게 되며, False가 한번이라도 나오면 재귀적으로 계속 False가 나와서 bipartite 함수내에서 dfs 함수의 최종 return은 False가 되며 결과적으로 -1이 출력된다.(이분그래프가 아니라는 의미.)

** 코드 설명
k(그래프 개수)번 만큼 for 문을 돌면서,
    v,e 를 입력받고, group에 대해 저장할 리스트인 visited를 v+1 길이로 생성(0번째 인덱스 쓰지않고, 1번 부터 쓰기위해 v+1 길이로 지정.)
    make_graph 함수에서 이중 리스트로 graph를 생성(역시 0번째 인덱스 쓰지않고, 1번 부터쓰기위해 graph 내부에 e+1개의 리스트 생성.)
    -> 양방향으로 그래프를 만들어 준다.
    ** visited와 graph에서 0번쨰 인덱스를 쓰지않고 1번 부터 쓰는 이유는, 문제에서 정점을 1번 부터 차례대로 주기 때문에 정점 번호를 인덱스와 동일하게 사용하기 위함이다.

    bipartite 함수는 graph와 visited를 입력으로 받아서
    bipartite_graph 값을 True로 주고,
    for문으로 graph에서 각 정점(v)을 반복하면서,
        visited가 0인 정점. 즉, 방문하지 않은 정점을 시작으로 dfs 함수를 호출하여 깊이 우선 탐색을 시작한다.
        dfs함수 내에서 start 정점을 방문한다.(방문했다는 사실은 visited의 start 인덱스에 group값을 줌으로써 start 정점을 방문했다고 표시)
        방금 방문한 start 정점을 기준으로 for문을 돌며
            start정점에 인접한 한 정점을 방문하지 않았다면,
                재귀적으로 dfs함수를 호출하는데, dfs함수의 반환값이 False라는 것은 방금 방문한 정점 visitied[start]과 start정점에 인접한 정점 i의 group이 같은 경우이다. 즉, 서로 인접해 있는데 group이 같은 경우로 이분그래프가 아닌 경우이다. -> line51
            line51 에서 방문한 정점 start와 그에 인접한 정점 i의 group이 다른 상태로 DFS가 모두 종료되면 True를 반환한다.
            즉, 그래프를 깊이 우선 탐색으로 group을 매겨가며 모두 탐색했는데 서로 인접한 두 정점의 group이 모두 달랐다는 의미로, 이분그래프라는 의미이다.
    결론적으로, 각 그래프에 대해 bipartite 함수내에서 dfs 함수의 최종 return이 True 라면 이분그래프라는 의미이고 1을 출력한다. 반대로  bipartite 함수내에서 dfs 함수의 최종 return이 False라면 이분그래프가 아니라는 의미이고 -1을 출력한다.
"""
def make_graph(f):
    graph = [[] for _ in range(v+1)]
    for i in range(1,e+1):
        start,end = map(int,f.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    return graph

def dfs(start, group, graph, visited):
    visited[start] = group
    for i in graph[start]:
        if visited[i] == 0:
            if dfs(i, -group, graph, visited) is False:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

def bipartite(graph,visited):
    bipartite_graph = True
    for i in range(1,v+1):
        if visited[i] == 0:
            if dfs(i, 1, graph, visited) is False:
                bipartite_graph = False
                break
    print('1' if bipartite_graph else '-1',end=' ')

with open('../dataset/rosalind_bip.txt') as f:
    k = int(f.readline())
    for i in range(k):
        f.readline() # remove empty space
        v,e = map(int,f.readline().split())
        
        visited = [0] * (v+1)
        graph = make_graph(f)

        bipartite(graph,visited)        