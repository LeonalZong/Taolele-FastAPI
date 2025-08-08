import asyncio

from utils import async_timed


async def greet(name, delay):
    await asyncio.sleep(delay)
    return f"Hello {name}!"
    
# @async_timed
# async def main():
#     result1 = await greet("Alice", 1)
#     print(result1)
#     result2 = await greet("Leonal", 2)
#     print(result2)
@async_timed
async def main():
    #并发运行必须要将协程包装成Task对象，才能够并发运行
    task1 = asyncio.create_task(greet("Alice",1))
    task2 = asyncio.create_task(greet("Leonal",2))

    #对创建好的任务进行await
    result1 = await task1
    result2 = await task2

    print(result1)
    print(result2)
    
   
if __name__ == "__main__":
    asyncio.run(main())