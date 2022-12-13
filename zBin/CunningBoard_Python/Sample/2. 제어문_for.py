# # Python
    # # Control Statement
        # # for in Statement
# # =======================================

# # for Item in Iterable
    # # # * Iterable  :  반복 가능한 객체 (문자열, 리스트, 튜플, range함수)
Str_1 = '1234'  
Str_A = 'ABCD'
List_1= [11, 12, 13, 14]
List_A= ["elem_A1", "elem_A2", "elem_A3", "elem_A4"]
# # 내장함수_range([start=0] , stop , [step=1])  :  순차적인 숫자를 가지는 <리스트>를 생성하는 함수
    # # # [start : 시작 숫자]
    # # # [stop : 끝 숫자]
        # # # # 끝 숫자는 포함되지 않음.
    # # # [step : 숫자 사이의 거리]
        # # # # 값이 0인 경우, 출력되지 않음.
        # # # # 값이 음수인 경우, 리스트 순서를 반대로 생성 , [  참고 : reversed(range(10))  ]
# range_1 = range(0,10)
# range_2 = range(10)
# print(range_1)
# print(range_2)
# # # # Case = [ Iterable = Str ]
# Test = Str_A
# for i in Test:
#     print(i)
# # # # Case = [ Iterable = range함수 ] , i = 0~9 (10개)
# Test = range(10)
# for i in Test:
#     print(i)
# # ----------
# Test = range(0,10)
# for i in Test:
#     print(i)
# # ----------------------------------------


# # continue
asd = "Asdasd"

for i in range(3):
    print(i)
else:
    print("a")
