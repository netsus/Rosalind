# coding: utf-8
"""
난이도 : 

문제 : 정점수(V) 와 간선 수(E)가 주어지고, (정점은 1 번 부터 ~ V 번 까지 존재한다.)
다음 줄 부터 시작정점 끝정점 가중치 가 E 개만큼 주어진다. (행 구분자)
1번 정점에서 각 정점까지 최단 거리를 공백을 구분자로 출력하시오. (1번 정점에서 도달 할 수 없는 정점이라면 -1 출력.)

알고리즘 : 
"""

import sys
import heapq

INF = sys.maxsize

# 다익스트라 알고리즘
def solve(adjacent, K):
    prev = [-1] * (len(adjacent) + 1)    # predecessor
    dist = [INF] * (len(adjacent) + 1)   # source로부터의 최소 거리 배열
    dist[K] = 0

    priority_queue = []
    heapq.heappush(priority_queue, [0, K])

    while priority_queue:
        # 거리가 제일 작은 노드 선택
        current_dist, here = heapq.heappop(priority_queue)

        # 인접 노드 iteration
        for there, length in adjacent[here].items():
            next_dist = dist[here] + length

            if next_dist < dist[there]:
                dist[there] = next_dist
                prev[there] = here
                heapq.heappush(priority_queue, [next_dist, there])

    return dist, prev

if __name__ == "__main__":
    with open('rosalind_dij.txt') as f:
        V,E = map(int,f.readline().split())
        adjacent = [{} for _ in range(V + 1)]
        for _ in range(E):
            u, v, w = map(int,f.readline().split())
            if v in adjacent[u]:
                adjacent[u][v] = min(adjacent[u][v], w)
            else:
                adjacent[u][v] = w

        dist, prev = solve(adjacent, 1)
        li3 = [i if i != INF else -1 for i in dist[1:-1]]
    print(*li3)
    