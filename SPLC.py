
# coding: utf-8

# In[23]:


"""
PROT 문제 응용. (PROT 문제 잘알아두기)

난이도 : 3.1

문제 : FASTA 파일 형식으로 서열 주어짐. 첫번째 서열이 main_seq이고, 나머지 서열은 intron으로 잘라버려야할 서열들
    exon부분에 대해 아미노산 서열 출력(가장 먼저있는 M으로 시작, Stop에서 종료)
    
알고리즘 : FASTA형식을 서열의 리스트로 바꿔주는 함수 make_seq_li
    서열의 리스트인 seq_li를 입력으로 받고, 첫번째서열을 main_seq으로 하고 
    for문을 이용해 나머지 서열을 replace함수를 이용해 제거
    main_seq은 DNA서열이므로, T를 U로 바꿔 RNA 서열로 변환
    RNA 서열에서 AUG로 시작하고, Stop으로 종료되는 서열을 찾아 아미노산 서열로 변환하여 출력해주는 함수 transcribe_translate 이용
"""

rna_amino_table = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G""".split()

codon_table = dict(zip(rna_amino_table[::2],rna_amino_table[1::2]))

def make_seq_li(file):
    seq_li=[];idx=-1
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            seq_li.append('')
            idx+=1
        else:
            seq_li[idx]+=line
    return seq_li

def transcribe_translate(seq_li):
    main_seq = seq_li[0]
    for i in seq_li[1:]:
        main_seq = main_seq.replace(i,'')

    seq = main_seq.replace('T','U')

    amino_seq=[];start=0
    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        sym = codon_table[codon]
        if sym=='M':
            amino_seq.append(sym)
            start=1
        elif sym=='Stop':
            break
        elif start==1:
            amino_seq.append(sym)
        else:
            continue
    return ''.join(amino_seq)        

file = open('rosalind_splc.txt','r')
seq_li = make_seq_li(file)
print(transcribe_translate(seq_li))

