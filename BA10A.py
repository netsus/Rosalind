
# coding: utf-8

# In[132]:


"""
난이도 : 3

문제 : 일련의 서열(seq)과 상태(states) 행렬 테이블(table)이 '--------'를 구분자로 주어진다.
    행렬 테이블을 바탕으로 서열이 형성될 확률값을 출력하시오. (단, 시작 확률은 동일하다고 가정.)

알고리즘 : make_input 함수는 주어진 형식의 file에 대해 '--------'을 구분자로 seq, states, table을 반환
    seq 변수는 주어진 서열을 문자열로 저장.
    states 변수는 주어진 상태에 대해 딕셔너리로 저장. ex) A B가 주어지면 {'A': 0, 'B': 1} 형식으로 저장
    table 변수는 주어진 확률 값에 대해 행,열을 갖는 이중 리스트로 저장. ex) A     B     가 주어지면 [[0.665, 0.335], [0.536, 0.464]]
                                                                          A 0.665 0.335             형식으로 저장.
                                                                          B 0.536 0.464
    caculate_probability 함수는 위의 함수에서 반환된 seq, states, table을 입력받아
    초기 확률을 probability 변수에 0.5로 초기화 하고 (시작 확률은 반,반으로 동일하다고 가정했기 때문)
    for 문을 통해 주어진 서열의 인덱스를 순차적으로 탐색하며
        2문자씩 가져와 첫문자를 row 변수에, 두번째 문자를 col 변수에 저장하여
        probabilty 에 *= 연산을 통해 table에서 row행 col열 값을 중첩하여 곱해나간다.
    그렇게 구한 probabilty를 출력
"""

def make_input(file):
    seq , states , pre_table = file.read().split('--------')
    seq = seq.strip()
#     print(seq)
    states = dict((state,idx) for idx,state in enumerate(states.strip().split()))
#     print(states)
    rows = pre_table.strip().split('\n')[1:]
    table = [list(map(float,col.split()[1:])) for col in rows]
#     print(table)
    return seq, states, table 

def caculate_probability(seq,states,table):
    # initial probablilty is 0.5
    probabilty = 0.5
    for idx in range(len(seq)-1):
        row,col = seq[idx], seq[idx+1]
        probabilty *= table[states[row]][states[col]]
    return probabilty

with open('rosalind_ba10a.txt') as file:
    seq, states, table = make_input(file)
    print(caculate_probability(seq,states,table))

