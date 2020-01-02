
# coding: utf-8

# In[150]:


"""
난이도 : 3

문제 : 행(k), 열(n)이 주어지고, 다음부터 k 행, n 열을 갖는 matrix가 주어진다.
    matrix의 각 행에 대해서, 1=< p < q <=n 에 대해, -row(p) == row(q) 가 존재하면 p와 q를 출력하고, 존재하지 않으면 -1 출력
    (각 행은 1 based)

알고리즘 : matrix의 각 행에 대해서,
    for문을 이용하여 각 행을 순차적으로 돌면서 나오는 숫자(A)에 대해, 그 행에서 해당 숫자(A) 뒷부분에 -A가 
    존재한다면
        해당 숫자의 1 based 인덱스와 -A를 행 오른쪽부터 탐색하여 1 based 인덱스를 출력한다.
    존재하지 않는 다면
        flag를 이용해 -1 출력
"""

def print_reverse_minus_same(matrix,k,n):
    flag=0
    for i in range(k):
        for j in range(n):
            row = matrix[i]
            if -row[j] in row[j+1:]:
                print(j+1,n - row[::-1].index(-row[j]))
                flag = 1
                break
        if flag == 0:
            print(-1)
        flag=0

with open('rosalind_2sum.txt') as file:
    # make input
    k,n = map(int,file.readline().rstrip().split())
    matrix=[]
    for row in file:
        matrix.append(list(map(int,row.rstrip().split())))
    #use function
    print_reverse_minus_same(matrix,k,n)

