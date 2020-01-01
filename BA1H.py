
# coding: utf-8

# In[87]:


"""
난이도 : 2.8

문제 : subseq, seq, d 가 세 줄로 입력된다.
    seq내에서 subseq과 최대 d 개 만큼 차이가 나는 똑같은 길이의 서열들의 시작 인덱스 부분을 출력하는 문제. (0_based)

알고리즘 : 
    mismatch_count 함수는 subseq과 pattern을 입력받아 서로 다른 염기가 몇개인지 반환해준다. 즉 mismatch 개수 반환해주는 함수
    (subseq과 pattern은 같은 길이의 문자열이다.)
    
    print_positions_mismatch 함수는 주어진 txt파일에서 subseq,seq,d 를 구분해서 입력받고,
    for문을 len(seq) - len(subseq) + 1 번 반복한다. ( 이 횟수는 seq에 대해 subseq 길이만큼 전체 탐색하겠다는 의미이다.)
        seq에서 subseq 길이만큼의 문자열을 pattern에 저장하고 mismatch_count함수를 호출하여 subseq과 pattern의 서열 차이값을 반환한다.
        반환값이 d 이하이면 해당 인덱스를 출력한다.
"""
def mismatch_count(subseq,pattern):
    s1 = ' '.join(subseq).split()
    s2 = ' '.join(pattern).split()
    cnt=0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt+=1
    return cnt

def print_positions_mismatch(file):
    pre_input = file.read().rstrip().split('\n')
    subseq, seq = pre_input[0:2]
    d = int(pre_input[2])
    
    for i in range(len(seq) - len(subseq) + 1):
        pattern = seq[i : i+len(subseq)]
        if mismatch_count(subseq,pattern) <= d:
            print(i,end=' ')

with open('rosalind_ba1h.txt') as file:
    print_positions_mismatch(file)

