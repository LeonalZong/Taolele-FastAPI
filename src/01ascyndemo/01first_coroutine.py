import asyncio

async def main():
    print("Hello")
    # 模拟异步操作，比如网络请求、文件读写等
    #需要在前面加await
    await asyncio.sleep(1)
    print("World")

if __name__ == "__main__":
    #创建一个协程对象，这样并不直接运行main函数，而是返回一个协程对象
    cor = main()
    # 运行协程对象，会自动调用main函数
    asyncio.run(cor)