
# coding: utf-8

# In[68]:


"""
문제 : 첫 줄에 node 수와 edge 개수가 주어지고, 
    다음줄 부터 edge 개수만큼 시작node와 연결된 node가 주어진다.
    node는 1번부터 차레대로 주어진다고 할때, 순서대로 degree를 출력하시오.
    
알고리즘 : file에서 숫자 2개로 이루어진 쌍을 한 원소로 갖는 리스트인 pair_li를 생성
    첫번째 숫자 쌍인 node수와 edge개수를 n,d에 저장
    node_li는 노드개수만큼 nested list를 갖는 이중리스트 생성
    
    for 문을 돌며
    두번째 숫자 쌍부터 node_li에 시작노드와 종료노드에 대해 앞,뒤로 모두 저장
    (예를들어, (1,2)라면 1번노드에 2저장, 2번노드에 1저장)
    
    모두 저장한 node_li에는 순서대로 각 노드에 연결된 다른 노드의 번호를 리스트로 갖게된다.
    1번 노드부터 degree를 출력.(답 형식에 맞게 공백을 구분자로 출력)
"""

def print_degree(file):
    pair_li = file.read().rstrip().split('\n')

    n,d = map(int,pair_li[0].split())

    node_li = [ [] for i in range(n)]

    for pair in pair_li[1:]:
        node,value=map(int,pair.split())
        node_li[node-1].append(value)
        node_li[value-1].append(node)

    print(*[len(degree) for degree in node_li])
    return None

file = open('rosalind_deg.txt','r')
print_degree(file)

