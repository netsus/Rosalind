
# coding: utf-8

# In[38]:


"""
문제 : FASTA형식의 파일을 입력받음 (서열의 길이는 모두 동일)
    모든 서열에 대해서, 0번째 염기부터 마지막 염기까지, ACGT 순으로 가장 많이나오는 염기들로만 서열을 만들고,
    모든 서열에대해 0번째 인덱스부터 마지막 인덱스까지 ACGT 순으로 각염기가 몇번씩 반복되는지 출력하시오.
    
알고리즘 : 먼저 FASTA형식의 파일을 입력받았을때 각 서열을 문자열 원소로 갖는 seq_li를 만드는 make_seq_li 함수를 정의
    seq_li를 입력으로 받아 각 인덱스 별로 빈도수가 가장 많은 염기를 갖는 서열 Consensus와
    각 인덱스별로 ACGT의 빈도수를 갖는 Profile을 print 해주는 print_Consensus_and_Profile함수를 정의
    
make_seq_li 함수의 주된 알고리즘은 FASTA파일을 입력으로 받아 for문에서 한줄씩 반복하며
'>'로 시작할때마다 인덱스를 하나씩 증가시키고, seq_li내에 빈문자열을 생성한뒤
'>'로 시작하지 않을때 해당 인덱스에 서열을 뒤로 붙여가며 저장한다.

print_Consensus_and_Profile 함수의 주된 알고리즘은 seq_li라는 이중리스트를 입력으로 받아 
각 서열의 길이는 모두 똑같으므로, 서열의 길이만큼 for문을 돌며 한번 반복할때마다
리스트 컴프리핸션으로 각 열(세로)을 base_li에 저장하고, 
answer_seq이라는 리스트에 ACGT의 빈도수가 가장 큰 염기를 하나씩 저장
ACGT_double_li 라는 4줄로된 이중 리스트에 첫줄부터 4번째 줄까지 각각, A, C, G, T의 빈도수를 하나씩 저장
for문이 끝나면
answer_seq과 ACGT_double_li를 정답 포맷에 맞게 출력
"""
def make_seq_li(file):
    seq_li=[] ; idx=-1
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            idx+=1
            seq_li.append('')
        else:
            seq_li[idx]+=line
    return seq_li

def print_Consensus_and_Profile(seq_li):
    length = len(seq_li[0])
    answer_seq=[]
    ACGT_double_li=[ [], [], [], [] ]
    for i in range(length):
        base_li = [k[i] for k in seq_li]
        ACGT='ACGT'
        ACGT_li = [ base_li.count(i) for i in ACGT]
        answer_seq.append( ACGT[ACGT_li.index(max(ACGT_li))] )
        for i in range(len(ACGT)):
            ACGT_double_li[i].append(ACGT_li[i])    

    print(''.join(answer_seq))
    for i in range(len(ACGT)):
        print(ACGT[i]+':',*ACGT_double_li[i] )

file = open('rosalind_cons.txt','r')
seq_li = make_seq_li(file)
print_Consensus_and_Profile(seq_li)

