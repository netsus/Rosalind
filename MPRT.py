
# coding: utf-8

# In[49]:


"""
난이도 : 3(알고리즘은 쉬운데, 라이브러리 활용이 필요)

문제 : uniprot_id 들을 입력받는다. 해당 uniprot_id들로 부터 uniport.org에서 fasta 파일을 읽어와서  N-glycosylation motif 가 있으면
    uniprot_id와 그 시작 인덱스를 출력하시오 (1_based)
    (N-glycosylation motif는 FASTA파일내에서  N{P}[ST]{P} 형식을 갖는 부분서열을 의미한다.
     즉, N으로 시작, 다음에 P외의 문자가 오고, 그 다음에 S or T가 오고, 그 다음에 P외의 문자가 오는 부분 서열.
     ex) NESH NETH 등등

알고리즘 : make input 부분에서 입력받은 uniprot_id 들을 uniprot_id_li(리스트)에 저장하고,
        for 문을 이용해 uniprot_id_li 에서 uniprot_id를 하나씩
            get_seq_from_uniprot 함수에 넣는다. 해당 함수에서는 uniprot_id를 urllib.request.urlopen()함수를 이용해 fasta 파일로
            f에 입력받는다. f는 바이트 형식이므로 uft-8 형식으로 decode 해주고, ID 와 seq를 변수에 저장하고 seq만 반환한다.
            위 함수에서 반환된 seq와 uniprot_id를 print_N_glycosylation_motif 함수에 입력한다.
            print_N_glycosylation_motif 함수에서는 re 라이브러리의 정규표현식을 이용하여 seq에 N-glycosylation motif가 있는지 조사한다.
            있다면 그 인덱스를 1_base로 idx_li(리스트)에 저장한다.
            리스트에 값이 존재한다면(N-glycosylation motif가 존재한다면)
                uniprot_id와 idx_li를 출력형식에 맞게 출력한다.

"""
import urllib
import re

def get_seq_from_uniprot(uniprot_id):
    f = urllib.request.urlopen('https://www.uniprot.org/uniprot/%s.fasta' %(uniprot_id))
    ID = f.readline().decode("utf-8").rstrip()
    seq = ''.join(f.read().decode("utf-8").rstrip().split('\n'))
    return seq

def print_N_glycosylation_motif(uniprot_id, seq):
    idx_li = [idx.start() + 1 for idx in re.finditer(r'(?=N[^P][ST][^P])', seq)]
    if idx_li:
        print(uniprot_id)
        print(*idx_li)
        

with open('rosalind_mprt.txt') as file:
    # make input
    uniprot_id_li = [line.strip() for line in file.readlines()]
    for uniprot_id in uniprot_id_li:
        # use function
        seq = get_seq_from_uniprot(uniprot_id)
        print_N_glycosylation_motif(uniprot_id,seq)


# In[65]:


uniprot_id


# In[73]:


for i in re.finditer(r'(?=N[^P][ST][^P])',seq):
    print(i.start(),i.end())

