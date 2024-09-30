import os
import sys

from modules.add import add

import sysconfig

# 설치된 라이브러리들의 경로 출력
print(sysconfig.get_paths()["purelib"])


if __name__ == "__main__":
    N = int(input("input 1: "))
    M = int(input("input 2: "))

    k = add(N, M)

    print(k)

    input("Press Enter to exit...")
