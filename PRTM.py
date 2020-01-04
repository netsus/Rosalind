
# coding: utf-8

# In[22]:


"""
난이도 : 1.2

문제 : protein_seq(단백질 문자열)이 주어진다. monoisotopic mass table을 참고하여 단백질 질량의 총합을 출력하시오.

알고리즘 : monoisotopic mass table을 { 단백질 symbol : 질량 } 형태의 table로 만들어주고,
    주어진 단백질 서열에 대해 질량값을 모두 더해서 출력.
"""

protein_mass_li = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 """.split()

protein_mass_table = dict(zip(protein_mass_li[::2], map(float,protein_mass_li[1::2])))

def print_total_weight(protein_seq):
    total_weight=0
    for prt in protein_seq:
        total_weight += protein_mass_table[prt]
    print(total_weight)

with open('rosalind_prtm.txt') as file:
    # make input
    protein_seq = file.readline().rstrip()
    # use function
#     print_total_weight(protein_seq)
    # short coding 
    print(sum([protein_mass_table[prt] for prt in protein_seq]))

