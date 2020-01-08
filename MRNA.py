
# coding: utf-8

# In[30]:


"""
난이도 : 1.5

문제 : 아미노산 서열이 주어지면, 가능한 RNA서열의 모든 경우의수 % 1,000,000를 출력하시오. (종결코돈의 경우의수 고려!)

알고리즘 : PROT 문제에서도 썼던 코돈 테이블을 가져와서 
    Counter를 이용하여 각 아미노산 별로 RNA 경우의수를 저장하여 amino_rna_num_table을 생성
    print_module_rna_num 함수는 rna 경우의수를 1,000,000로 나눈 나머지를 출력하는 함수이다.
        주어진 아미노산 서열(protein_string)을 입력으로 받고 각각 서열을 amino_rna_num_table에서 경우의수로 변환하여
        total_mass에 곱해준다. 모두 곱했으면 마지막에 amino_rna_num_table['Stop'] 즉, 종결코돈의 경우의 수까지 곱하고
        1,000,000으로 나눈 나머지를 출력한다.
"""
from collections import Counter

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

amino_rna_num_table = Counter()
# make 
for i in rna_amino_table[1::2]:
    amino_rna_num_table[i] += 1

def print_module_rna_num(protein_string):
    total_mass=1
    for mass in protein_string:
        total_mass *= amino_rna_num_table[mass]
    total_mass *= amino_rna_num_table['Stop']
    print(total_mass%1000000)

with open('rosalind_mrna.txt') as file:
    # make input
    protein_string = file.readline().rstrip()
    # use function
    print_module_rna_num(protein_string)

