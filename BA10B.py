
# coding: utf-8

# In[ ]:


"""
난이도 : 3 (BA10A 문제의 응용 버전. 거의 비슷함)

문제 : 일련의 서열(string)과 상태(str_states) 그리고 일련의 경로(path)와 상태(path_states) 그리고,행렬 테이블(table)이 
    '---------'를 구분자로 주어진다.
    행렬 테이블의 확률 값을 바탕으로 path가 주어졌을때, string이 될 조건부 확률을 구하시오.

알고리즘 : make_input 함수는 주어진 형식의 file에 대해 '---------'을 구분자로 string, path, str_states, path_states, table을 반환
    string 변수와 path 변수는 주어진 서열과 경로를 문자열로 저장.
    str_states 변수와 path_states 변수는 주어진 상태에 대해 딕셔너리로 저장. 
    table 변수는 주어진 확률 값에 대해 행,열을 갖는 이중 리스트로 저장. 
    
    caculate_probability 함수는 위의 함수에서 반환된 string, path, str_states, path_states, table을 입력받아
    BA10A 문제와 다르게 초기 확률은 그냥 1.
    for 문을 통해 string 과 path를 zip함수를 통해 동시에 한글자씩 가져온다.
        string에서 가져온 한글자는 str_one, path에서 가져온 한 글자는 path_one에 저장
        probabilty 에 *= 연산을 통해 table에서 path_states[path_one]행 str_states[str_one]열 값을 중첩하여 곱해나간다.
    그렇게 구한 probabilty를 출력
"""

def make_input(file):
    string , str_states , path, path_states, pre_table = file.read().split('--------')
    string = string.strip()
    path = path.strip()


    str_states = dict((state,idx) for idx,state in enumerate(str_states.strip().split()))
    path_states = dict((state,idx) for idx,state in enumerate(path_states.strip().split()))

    rows = pre_table.strip().split('\n')[1:]
    table = [list(map(float,col.split()[1:])) for col in rows]
    return string, path, str_states, path_states, table

def calculate_probability(string, path, str_states, path_states, table):
    probabilty = 1
    for str_one, path_one in zip(string,path):
        probabilty *= table[path_states[path_one]][str_states[str_one]]
    return probabilty

with open('rosalind_ba10b.txt') as file:
    print(calculate_probability(*make_input(file)))

