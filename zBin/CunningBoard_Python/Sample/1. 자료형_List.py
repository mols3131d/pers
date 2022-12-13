# # Python
    # # 자료형
        # # List
# # =======================================
# 목차
# 개요
# 하급 , 형태, 생성, 삭제, 요소 추가, 요소 제거
# 중급 , 입력, 출력, 
# 상급 , 

# # 1]  개요
# # 1-1] 


# # 2] 하급
# # 2-1] 형태
# # List Example
Str_1 = "1 2 3 4"
List_1 = [11, 12, 13, 14]
List_2 = [21, 22, 23, 24]
List_A = ["elem_A1", "elem_A2", "elem_A3", "elem_A4"]
List_B = ["B1", "B2", "B3", "B4"]



# # 3] 중급
# # 3-1] 입력


# # 3-2] 출력

    # # print(List)
TestList_1 = List_1
print("print(List_1) : ", TestList_1)
print("print(*List_1) : ", *TestList_1)
print("print(*List_1, sep = \"\\n\") : ", *TestList_1, sep = "\n")

# Str.split()  :  [특정 문자로 구분된 문자열] -> 리스트
TestStr_1 = Str_1
print(TestStr_1)
TestVar_1 = str.split()

# len(List)
TestList_1 = List_1
TestVar_1 = len

# List.remove('elem')  :  'elem'이라는 요소(elem, element)를 삭제. 
# 만약, 해당 요소가 리스트 내에 복수가 존재하는 경우, index가 가장 낮은 요소를 삭제.
List_1.remove('11')
# 그래서, 해당 요소를 모두 삭제하기 위해, 반복문을 활용하여 삭제.
while '11' in List_1:
    List_1.remove('11')

# List.pop('elem')  :  'elem'이라는 요소(elem, element)를 삭제. 
# 인덱스가 11인 요소를 삭제
List_1.pop(11)
# List.clear()  :  리스트 내의 모든 요소를 삭제.
# 리스트의 모든 요소를 삭제
List_1.clear()
# del Lsit[0]  :  del 키워드로 index가 0인 요소를 삭제
# del 키워드를 통해 인덱스가 1인 요소를 삭제
del List_1[1]
del List_1[1:2]

# 2차원 이상 list 의 합 구하기, 원하는 답은 9
from typing import List
lst = [ [ 1, [1,1,1,1], 1 ] , [ 1,1,1 ] ]
def sum_list(lst, res = 0):    
    for i in lst:
          if type(i) == list:
                res += sum_list(i)
          else:
                res += i
    return res
print(sum_list(lst))






# List to Dict
# https://security-nanglam.tistory.com/427
# 1. Dictionary Comprehesion(딕셔너리 컴프리헨션) 이용
string_list = ['A','B','C']
dictionary = {string : 0 for string in string_list}
print(dictionary)
# => {'A': 0, 'B': 0, 'C': 0}

string_list = ['A','B','C']
dictionary = {string : i for i,string in enumerate(string_list)}
print(dictionary)
# => {'A': 0, 'B': 1, 'C': 2}


# 2. dict.fromkeys(key, value) 이용
string_list = ['A','B','C']
dictionary = dict.fromkeys(string_list,0)
print(dictionary)
# => {'A': 0, 'B': 0, 'C': 0}

#Value에 아무것도 적지 않는다면 value는 None으로 됩니다.

string_list = ['A','B','C']
dictionary = dict.fromkeys(string_list)
print(dictionary)
# => {'A': None, 'B': None, 'C': None}

# 3. list의 값을 value로 갖는 dict 만들기 (1번 방법에서 key와 value가 반대로)
string_list = ['A','B','C']
dictionary = {i : string_list[i] for i in range(len(string_list))}
print(dictionary)
# => {0: 'A', 1: 'B', 2: 'C'}
 
# 이번에는 두개의 list 가지고 놀아봅시다..!
# string_list = ['A','B','C']
# int_list = [1, 2, 3]

# 위 두개의 리스트를 key : value 형식으로 바꿔봅시당~
# 1. zip 사용하여 묶기
# string_list = ['A','B','C']
# int_list = [1, 2, 3]
# dictionary = dict(zip(string_list, int_list))
# print(dictionary)
# => {'A': 1, 'B': 2, 'C': 3}

# 물론 string_list 와 int_list의 순서를 바꾸면 key와 value도 변경됩니다.
# string_list = ['A','B','C']
# int_list = [1, 2, 3]
# dictionary = dict(zip(int_list, string_list))
# print(dictionary)
# => {1: 'A', 2: 'B', 3: 'C'}

# 그러면 tuple로 되어있는 list는 dict으로 어떻게 바꾸나요!
# tuple_list = [('A',1), ('B',2), ('C',3)]
# 이러한 튜플 리스트가 있을때.. dict으로 변경하기 위해서는 dict()을 사용해주면 됩니다.
# tuple_list = [('A',1), ('B',2), ('C',3)]
# dictionary = dict(tuple_list)
# print(dictionary)
# => {'A': 1, 'B': 2, 'C': 3}