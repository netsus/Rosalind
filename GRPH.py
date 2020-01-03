
# coding: utf-8

# In[44]:


"""
난이도 : 2.9

문제 : FASTA 형식으로 여러 ID와 DNA 서열을 준다.
    각 ID에 따른 DNA 서열의 뒷부분 세 염기가 다른 ID의 첫부분 3 염기와 같다면 ID를 짝지어 출력하시오.
    
알고리즘 : make_seq_dict 함수는 FASTA형식의 file에서 ID와 dna 서열을 분리하여 seq_di에 딕셔너리 형태로 저장 및 반환
    suffix_to_prefix 함수는 seq_di를 입력으로 받고, ID와 서열을 각각 리스트의 형태로 ID_li,seq_li에 저장
    for 문을 통해 각 서열을 순차적으로 탐색하며 
        앞부분 3염기가 다른 서열의 뒷부분 3염기와 같다면 해당 ID를 짝지어 출력 (이때, 같은 아이디가 짝지어 출력되지 않도록 한다.)
        
    
    처음에 FASTA 파일을 make_seq_dict 함수를 이용해 seq_di에 저장하고 suffix_to_prefix 함수에 입력하여 서로 다른 ID간에 suffix 3염기와
        prefix 3염기가 일치하는 모든 ID 쌍을 출력한다.
"""
def make_seq_dict(file):
    seq_di = dict()
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            ID = line[1:]
            seq_di[ID] = ''
        else:
            seq_di[ID] += line
    return seq_di

def suffix_to_prefix(seq_di):
    ID_li = list(seq_di.keys())
    seq_li = list(seq_di.values())

    for idx in range(len(ID_li)):
        prefix = seq_li[idx][-3:]
        suffix_li = [ seq[:3] for seq in seq_li ]
        suffix_idx = -1
        for i in range(suffix_li.count(prefix)):
            suffix_idx = suffix_li.index(prefix,suffix_idx+1)
            if idx != suffix_idx:
                print(ID_li[idx],ID_li[suffix_idx])       

with open('rosalind_grph.txt') as file:
    seq_di = make_seq_dict(file)
    suffix_to_prefix(seq_di)

