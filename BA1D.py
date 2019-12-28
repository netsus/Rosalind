
# coding: utf-8

# In[31]:


"""
난이도 : 1.7

문제 : substring과 전체서열이 주어지면, 전체 서열중 substring이 포함되는 시작 인덱스 출력 (0-based)
    (SUBS 문제와 거의 유사함)
    
알고리즘 : 전체서열을 for문으로 반복하여 substring 길이만큼씩 가져와서 substring과 일치하는지 일일이 검사
    일치할때마다 시작인덱스를 index_li에 append
    for문이 종료되면 index_li를 정답 포맷에 맞게 출력"""

def subs2(total_seq,substring):
    c = len(total_seq) - len(substring) + 1
    index_li=[]
    for i in range(c):
#         print(total_seq[i:i+len(substring)]) # 포함되는 substring 인지 출력하여 확인
        if total_seq[i:i+len(substring)]==substring:
            index_li.append(i)
    return print(*index_li) # str(' '.join(map(str,index_li)))

with open('rosalind_ba1d.txt','r') as file:
    substring, total_seq = file.read().rstrip().split('\n')
subs2(total_seq,substring)

