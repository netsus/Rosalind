
# coding: utf-8

# In[82]:


"""
난이도 : 2

문제 : 6개의 수를 입력받는다.
    각각 AA-AA  AA-Aa  AA-aa  Aa-Aa  Aa-aa  aa-aa 쌍의 개수이다. 모두 2명의 자녀를 낳는데 우성을 띄는 자녀의 개체수를 출력하시오.
    
알고리즘 : 입력은 six_integers 에 리스트의 형태로 저장한다.
    각 쌍마다 자식의 유전형의 경우의수는 총 4가지이다. 그중에서 우성 경우의수를 six_dominant_case 에 리스트형태로 저장한다.
    우성 개체수는 (우성이 태어날 확률)*(자녀의 총 개체수)로 나타낼 수 있다.
        (우성이 태어날 확률)은 6쌍에 대해 (우성이 태어날 경우의수) / (전체 경우의 수)로 나타낼 수 있다.
            우성이 태어날 경우의 수 : dominant_case는 6쌍이 낳은 자녀중 우성인 모든 개체수이다.
            전체 경우의 수 : total_case는 6쌍이 각각 4가지 유전형의 자녀를 갖는 모든 경우의수이다.
        (자녀의 총 개체수)는 6쌍이 모두 2명씩 낳는 모든 개체수이다.
    위의 과정을 거쳐 (우성이 태어날 확률)*(자녀의 총 개체수)를 계산하여 출력하면 된다.
"""
    
def calculate_dominant_number(six_integers,six_dominant_case):
    total_case = sum(six_integers) * 4
    total_offspring = sum(six_integers) * 2

    dominant_case = 0
    for i in range(6):
        dominant_case += six_integers[i]*six_dominant_case[i]
    print( dominant_case/total_case * total_offspring)

with open('rosalind_iev.txt') as file:
    #make input
    six_integers = list(map(int,file.readline().rstrip().split()))
    six_dominant_case = [4,4,4,3,2,0]
    
    #use function
    calculate_dominant_number(six_integers,six_dominant_case)
    
    #short cut
#     print( sum([a*b for a,b in zip(six_integers,six_dominant_case)])/2 )

