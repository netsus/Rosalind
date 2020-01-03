
# coding: utf-8

# In[65]:


"""
난이도 : 4.5

문제 : FASTA 형식으로 DNA 서열 1개가 최대 1kbp로 주어진다.
    해당 서열을 seq에 저장하고, seq과 seq의 reverse 상보서열에 대해서 모든 ORF부분의 아미노산을 출력해라. (중복제거)
    
알고리즘 : reverse_complement 함수는 서열을 입력받은 reverse 상보서열을 반환해주는 함수
    make_seq 함수는 FASTA형식의 파일을 입력받아 서열부분만 반환해주는 함수
    ORF_print_amino_seq 함수는 dna 서열을 입력받아 rna로 변환하고, AUG로 시작하는 모든 부분서열을 translate 함수에 전달하고,
    반환된 아미노산 서열을 amino_li에 모두 저장후 반환
    translate 함수는 AUG로 시작하는 rna 서열이 입력된다는 가정하에 번역되는 아미노산 서열을 반환 (종결코돈으로 정상 종료된 서열만 반환)
    
    
    주어진 파일을 make_seq 함수를 이용해 DNA서열만 seq에 저장하고, 
    seq과 reverse_complement함수를 이용한 역상보seq을 ORF_print_amino_seq함수에 입력으로 준다.
        seq과 역상보seq이 각각 ORF_print_amino_seq함수에서 정상 종료된 아미노산 서열로 모두 반환된다.
    반환된 것을 집합 amino1과 amino2에 저장하고 합쳐서 리스트로 만든뒤 순차적으로 출력한다.
        (집합에 넣는 이유는 중복된 서열 제거를 위해서이다.) 
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

complement_DNA_table = str.maketrans("ATGC","TACG")
complement_RNA_table = str.maketrans("AUGC","UACG")

def reverse_complement(seq, rna=False):
    if rna:
        return seq[::-1].translate(complement_RNA_table)
    else:
        return seq[::-1].translate(complement_DNA_table)
    
def make_seq(file):
    ID = file.readline().rstrip()
    seq=''
    for line in file:
        seq += line.rstrip()
    return seq

def ORF_print_amino_seq(dna_seq):
    rna_seq = dna_seq.replace('T','U')
    idx = -1;amino_li = list()
    for i in range(rna_seq.count('AUG')):
        idx = rna_seq.index('AUG', idx + 1)
        amino_seq = translate(rna_seq[idx:])
        if amino_seq:
            amino_li.append(amino_seq)
    return amino_li

def translate(rna_seq):
    amino_seq='';normal_exit=0
    for i in range(0,len(rna_seq),3):
        codon = rna_seq[i:i+3]
        if len(codon)==3:
            sym = codon_table[codon]
        else:
            break
        if sym=='Stop':
            normal_exit = 1
            break
        amino_seq += sym
    if normal_exit == 1:
        return ''.join(amino_seq)

with open('rosalind_orf.txt') as file:
    seq = make_seq(file)
    amino1 = set(ORF_print_amino_seq(seq))
    amino2 = set(ORF_print_amino_seq(reverse_complement(seq)))
    for amino in list(amino1.union(amino2)):
        print(amino)

