# 임의의 여러 줄을 입력받아야 하는 문제

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break


import sys
for line in sys.stdin:
     a, b = map(int, line.split())
     print(a + b)