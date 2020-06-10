# coding: utf-8
"""
난이도 : 

문제 : 정점수(V) 와 간선 수(E)가 주어지고, (정점은 1 번 부터 ~ V 번 까지 존재한다.)
다음 줄 부터 시작정점 끝정점 가중치 가 E 개만큼 주어진다. (행 구분자)
1번 정점에서 각 정점까지 최단 거리를 공백을 구분자로 출력하시오. (1번 정점에서 도달 할 수 없는 정점이라면 -1 출력.)

알고리즘 : 
"""

import sys

INF = sys.maxsize
with open('rosalind_dij2.txt') as f:
    V,E = map(int,f.readline().split())
    graph = [[INF]*V for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int,f.readline().split())
        graph[u-1][v-1] = w
        

# 방문했는지
s = [0]*V
# 1번 정점에서 시작. d는 각 정점까지의 최단거리
d = [0] + [INF]*(V-1)

while 1:
    