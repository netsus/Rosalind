
# coding: utf-8

# In[2]:


from Bio import ExPASy
from Bio import SwissProt

def print_bio_process(file):
    Uniprot_id = file.read().rstrip()
    handle = ExPASy.get_sprot_raw(Uniprot_id)
    rec = SwissProt.read(handle)
    bio_process = [ i[2][2:] for i in rec.cross_references if i[0]=='GO' and i[2].startswith('P') ]
    print('\n'.join(bio_process))

with open('rosalind_dbpr.txt','r') as file:
    print_bio_process(file)

