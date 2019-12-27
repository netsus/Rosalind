
# coding: utf-8

# In[32]:
"""
문제: 주어진 RNA 서열을 CONDON Table에 따라 아미노산 서열로 번역하여 출력하시오.
알고리즘 : RNA 코돈과 아미노산 symbol을 딕셔너리로 만들고,
RNA 서열을 입력으로, 아미노산 서열을 출력으로 하는 translate함수를 만듦.
단 종결코돈은 symbol을 Stop으로 지정하여 해당 코돈이 나오면 멈추도록 함."""

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

def translate(seq):
    amino_seq=list()
    for i in range(0,len(seq),3):
        sym=codon_table[seq[i:i+3]]
        if sym=='Stop':
            break
        amino_seq.append(sym)
    return ''.join(amino_seq)

seq=input()
translate(seq)

