# coding: utf-8
"""
난이도 : 6.5

문제 : 처음에 그래프 개수(k)가 주어지고, 
한줄 띄고, 정점 개수(v)와 간선 개수(e)가 주어지고, 다음줄에 시작 정점과 도착 정점 (방향 그래프)이 주어진다. -> 이렇게 그래프 개수만큼 주어진다.
주어진 방향 그래프에 대해 사이클이 있으면(cyclic) -1, 사이클이 없으면(acylcic) 1을 출력.


알고리즘 : 
"""
import networkx as nx
from IPython.core.display import Image
from networkx.drawing.nx_pydot import to_pydot

def make_graph(g,f,v,e):
    for i in range(1,e+1):
        start,end = map(int,f.readline().split())
        g.add_edge(start,end)
    return g

with open('rosalind_dag.txt') as f:
    k = int(f.readline())
    for i in range(k):
        f.readline()
        v,e = map(int,f.readline().split())
        g = nx.DiGraph()
        graph = make_graph(g,f,v,e)
        try:
            nx.find_cycle(graph,orientation='original')
            print(-1,end=' ')
        except:
            print(1,end=' ')
