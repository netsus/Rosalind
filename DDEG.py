
# coding: utf-8

# In[81]:


"""
문제 : 첫 줄에 node 수와 edge 개수가 주어지고, 
    다음줄 부터 edge 개수만큼 시작node와 연결된 node가 주어진다.
    node는 1번부터 차례대로 주어진다고 할때,
    1번 노드부터 이웃한 노드의 degree의 총합을 순서대로 출력하시오.

알고리즘 : file에서 숫자 2개로 이루어진 쌍을 한 원소로 갖는 리스트인 pair_li를 생성
    첫번째 숫자 쌍인 node수와 edge개수를 n,d에 저장
    node_li는 노드개수만큼 nested list를 갖는 이중리스트 생성
    
    for 문을 돌며
    두번째 숫자 쌍부터 node_li에 시작노드와 종료노드에 대해 앞,뒤로 모두 저장
    (예를들어, (1,2)라면 1번노드에 2저장, 2번노드에 1저장)
    
    모두 저장한 node_li에는 순서대로 각 노드에 연결된 다른 노드의 번호를 리스트로 갖게된다.
    
    node_li에 대해 for문을 돌며
    각 원소(각 node에 대해 연결된 노드 번호 = 이웃한 노드 번호)에 대해 다시 for문을 돌며
        이웃한 노드 에 연결된 degree를 neighbor_degree에 더해준다
    그러면 차례대로 1번 노드부터 이웃한 노드들의 degree합이 출력되고 end=' '로 다음 출력을 공백을 구분자로 받는다.
"""

def print_neighbors_degree(file):
    pair_li = file.read().rstrip().split('\n')

    n,d = map(int,pair_li[0].split())

    node_li = [ [] for i in range(n)]

    for pair in pair_li[1:]:
        node,value=map(int,pair.split())
        node_li[node-1].append(value)
        node_li[value-1].append(node)

    for node in node_li:
        neighbor_degree=0
        for i in node:
            neighbor_degree+=len(node_li[i-1])
        print(neighbor_degree,end=' ')
    return None

file = open('rosalind_ddeg.txt','r')
print_neighbors_degree(file)

