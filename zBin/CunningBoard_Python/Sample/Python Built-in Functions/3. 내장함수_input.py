# # Python
    # # 
        # # input()
# # =======================================


# # sys.stdin.readline()
    # # sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다.
    # # 만약 3을 입력했다면, 3\n 이 저장되기 때문에, 개행문자를 제거해야 합니다.
    # # 변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 합니다.

# # # Case : 고정의 1개의 정수 입력받는 경우
import sys
Test = int(sys.stdin.readline())

# # # Case : 미정의 X개의 정수를 한 줄에 입력 받는 경우
import sys
a,b,c = map(int,sys.stdin.readline().split())

# # # Case : [임의의 N의 값]과 [임의의 정수 N줄]을 입력 받아 2차원 리스트에 저장
# 입력 예시
# 5
# 1 1
# 12 34
# 5 500
# 40 60
# 1000 1000
import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

# # # Case : 문자 N 줄을 입력 받아 리스트에 저장
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
