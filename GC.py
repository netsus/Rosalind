
# coding: utf-8

# In[74]:


"""
문제 : fasta 포맷의 DAN string이 주어진다. GC함량이 가장 높은 ID와 GC 함량을 출력하시오.
알고리즘 : 주어진 fasta format의 파일을 입력받아 ID와 sequence를 분리해서 seq_dict라는 dictionary에 저장.
        (-> fasta 포맷의 입력에 대해 ID와 seq로 분리하여 다른 문제에도 활용 가능)
        저장된 딕셔너리를 반복하며 GC 함량의 최대값이 갱신될때 마다 GC함량과 ID를 각각 highest_GC,highest_ID에 저장
        반복문이 종료되면 ID와 GC함량 출력"""
f = open('rosalind_gc.txt','r')
fl = f.read()
fq_list = fl.split('\n')

seq_dict = dict() # ID와 sequence를 분리 저장할 dictionary
flag = 1
for i in fq_list[:-1]:
    if i[0] == '>':
        if flag == 0:
            seq_dict[name] = seq
        name = i
        flag = 1
    elif flag == 1:
        seq = i
        flag = 0
    else:
        seq += i
seq_dict[name] = seq

highest_GC=0
for k,v in seq_dict.items(): # 반복하며 GC 함량의 최대치 갱신될때마다 highest_GC, highest_ID에 저장
    GC = (v.count('G') + v.count('C')) / len(v) * 100
    if GC > highest_GC:
        highest_GC=GC
        highest_ID=k
        
print(highest_ID[1:])
print(highest_GC)

