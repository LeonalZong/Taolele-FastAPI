from functools import wraps
import time


def async_timed(func):
    @wraps(func)
    # 装饰器函数，用于计算异步函数的执行时间
    #*args, **kwargs 表示接收任意数量的位置参数和关键字参数
    async def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started, 参数: {args}, {kwargs}")
        start = time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.time()
            total = end - start
            print(f"Function {func.__name__} took {total:.4f} seconds to execute")
    return wrapper
        
    
