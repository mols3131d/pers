import asyncio


# 비동기 함수 정의
async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay} seconds")


async def main():
    # 세 개의 비동기 작업을 동시에 처리
    await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 3),
    )


# 이벤트 루프에서 실행
asyncio.run(main())
