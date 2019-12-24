
# coding: utf-8

# In[157]:


'''
문제 : k는 AA, m은 Aa, n은 aa의 개체수.
    전체 개체에 대해 무작위로 짝짓기를 하여 우성이 나올 확률을 계산하시오.
알고리즘 : 전체 개체에 대해 모든 경우의 수를 직접 계산.
    kk km kn / mk mm mn / nk nm nn 이 9가지가 모든 경우의 수
    각 확률을 계산하여 모두 합한 것을 반환'''
f = open('rosalind_iprb.txt','r')
fl = f.read().rstrip()
k,m,n=map(int,fl.split()) # 입력된 숫자 3개를 각각 k,m,n에 저장

total = k + m + n

kk = k / total * (k-1)/(total-1)
km = k / total * m/(total-1)
kn = k / total * n/(total-1)

mk = m / total * k/(total-1)
mm = m / total * (m-1)/(total-1)*3/4
mn = m / total * n/(total-1)*2/4

nk = n / total * k/(total-1)*4/4
nm = n / total * m/(total-1)*2/4
nn = n / total * (n-1)/(total-1)*0

print(kk+km+kn+mk+mm+mn+nk+nm+nn)

