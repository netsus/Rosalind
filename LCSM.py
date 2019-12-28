
# coding: utf-8

# In[249]:


"""
난이도 : 3 (long_common_seq 구할때 중첩 for문을 쓰는 경우)
(동적계획법으로 O(n)시간으로 풀면 난이도 : 4.5)

문제 : FASTA 형식으로 여러 서열이 주어질때, 모든 서열에서의 공통서열중 길이가 가장 긴 서열은?

알고리즘 : FASTA형식에서 서열부분만 리스트형태로 만든것 -> seq_li (함수 make_seq_li 이용)
    seq_li에서 가장 짧은 서열 구하기 -> shortest (함수 find_shortest이용 -> 시간 줄이기 위해서 가장 짧은서열 사용)
    shortest의 부분서열중에서 seq_li에 모두 포함되는 가장 긴 서열구하기 -> long_common_seq (함수 find_long_common 이용)
    
    find_long_common 함수에서 for문 한 루프에 하는일
    shortest 서열에 대해, 전 루프보다 한칸 오른쪽으로 이동
    
        이동해서 1만큼 길어진 서열이 seq_li의 서열에 모두 포함된다면 해당 서열을 long_common_seq에 저장하고,
        idx(서열의 시작부분 인덱스)를 그대로 두기위해 -1 해준다.
    
        이동해서 1만큼 길어진 서열이 seq_li에 포함되지 않는다면 앞부터 기존의 long_common_seq 만큼 길이에 대해 한칸씩 이동하며 확인한다.
        더 짧은 서열은 볼 필요가 없다. (기존의 long_common_seq 보다 짧은것은 어차피 long_common_seq이 될 수 없으니까)
"""
def make_seq_li(file):
    seq_li=[];idx = -1
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            seq_li.append('')
            idx+=1
        else:
            seq_li[idx]+=line
    return seq_li

def find_shortest(seq_li):
    short_len=len(seq_li[0])
    shortest=seq_li[0]
    for i in seq_li:
        if len(i) < short_len:
            shortest=i
            short_len = len(i)
    return shortest

def find_long_common(seq_li,shortest): # 최대 부분 배열 동적계획법 알고리즘 응용 O(n)
    idx=0;seq=''
    for i in range(len(shortest)):
        seq = shortest[idx:i+1]
        idx+=1
        if all([seq in s for s in seq_li]):
            long_common_seq=seq
            idx-=1
    return long_common_seq

with open('rosalind_lcsm.txt','r') as file:
    seq_li = make_seq_li(file)
    shortest = find_shortest(seq_li)
    print(find_long_common(seq_li,shortest))

