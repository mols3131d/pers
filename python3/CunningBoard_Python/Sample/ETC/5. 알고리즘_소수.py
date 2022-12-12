# 하나의 숫자 N이 소수인지 확인하는 알고리즘

# for N in range(2, 999999):
#     for i1 in range(2, int((N**(1/2)))+1 ):
#         if N % i1 == 0:
#             return 0
#     return 1

def checkPrimenumber1(N):
    for i1 in range(2, int((N**(1/2)))+1 ):
        if N % i1 == 0:
            return 0
    return 1

def checkPrimenumber2(N):
    if (N % 2 == 0) and (N ==2) :
        return 1
    elif (N % 2 == 0) and (N !=2) :
        return 0
    for i1 in range(3, int((N**(1/2)))+1 , 2 ):
        if N % i1 == 0:
            return 0
    return 1

def checkPrimenumber3(N):
    if 1 >= N :
        return 0
    elif 2 == N:
        return 1
    elif N % 2 == 0:
        return 0
    for i1 in range(3, int((N**(1/2)))+1 , 2 ):
        if N % i1 == 0:
            return 0
    return 1


# 특정 수 범위에 존재하는 소수 찾는 알고리즘 : 에라토스테네스의 체
