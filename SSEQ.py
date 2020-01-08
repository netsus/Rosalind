
# coding: utf-8

# In[99]:


"""
난이도 : 2.2

문제 : FASTA 포맷으로 서열 s와 t를 입력받는다. 서열 s 내에서 서열t의 각 염기들이 몇번째 인덱스에 존재하는지 순서대로 출력(1-based)
    답이 여러개일 수있으니 아무거나 출력하시오. 
    (단, 서열 t의 한 염기를 s에서 찾으면, 서열 t의 다음 염기는 서열s에서 찾은 부분 다음에 나옴. 즉, 서열은 오름차순으로만 출력됨)

알고리즘 : make_seq_li 함수는 FASTA파일을 입력받으면 서열부분만 반환하는 함수
        substring_location 함수는 서열 s,t가 있는 리스트를 입력받아 서열 s내에서 서열 t의 각 염기 위치를 1-based로 출력.
        
        substring_location의 알고리즘은
        for문을 서열 t 길이만큼 돌면서
            t의 첫글자에 대해 인덱스 0부터 찾고, 찾은 인덱스를 idx에 저장
            idx 출력한다.
            
            (다음 포문에서는 t의 두번째 글자에 대해 idx + 1 부터 찾는다. 즉, 다음글자 부터 찾음.
            이 과정을 반복)
"""
def make_seq_li(file):
    seq_di = {}
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            ID = line[1:]
            seq_di[ID] = ''
        else:
            seq_di[ID] += line
    return list(seq_di.values())


def substring_location(seq_li):
    s,t = seq_li
    idx = -1
    for i in range(len(t)):
        idx = s.index(t[i] , idx + 1)
        print(idx + 1)

with open('rosalind_sseq.txt') as file:
    seq_li = make_seq_li(file)
    substring_location(seq_li)

