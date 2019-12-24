'''
문제 : 길이가 같은 두 서열 입력받아 서로 다른 염기 개수가 몇개인지 출력
알고리즘 : 반복하며 비교해서 다르면 cnt += 1 '''
f = open('rosalind_hamm.txt','r')
fl = f.read().split('\n')

cnt=0
seq1,seq2=fl[:-1]
for i in range(len(fl[0])):
    if seq1[i]!=seq2[i]:
        cnt+=1
print(cnt)
