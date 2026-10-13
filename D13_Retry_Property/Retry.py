import time
from functools import wraps
import random

call_count = {}
def retry(max_attempts = 3,delay = 1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for attempt in range(1,max_attempts+1):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise 
                    print(f"第{attempt}次失败，{delay}s后重试")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts = 2,delay = 1)
def flaky_api():
    call_count["flaky_api"] = call_count.get("flaky_api",0) + 1
    if call_count["flaky_api"] < 3:
        raise ConnectionError("网络抖动")
    return "OK"


print(flaky_api())
print(flaky_api.__name__)