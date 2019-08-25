import multiprocessing as mp
import itertools
import time
import os
from functools import wraps #用途就在於讓使用 decorator 的函式，能夠正確將 name 及 docstring 顯示出來。
#from threading import Thread



result = mp.Array('d', [-1]*10)

def run_async(func):
    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = mp.Process( target=func, args=args, kwargs=kwargs )
        func_hl.start()
        return func_hl
    return async_func


@run_async
def sum(a, b, thread_number):
    global result
    s = 0
    print("thread_num", thread_number, "pid:", os.getpid(), "memory", id(a), id(b), id(s))
    for i  in range(a, b+1):
        s+=i
    #print(s)
    result[thread_number] = s
    return s


def supervisor():
    mp_pool = []

    for i in range(10):
        mp_pool.append(sum(1, 1000000, i))

    for i in range(10):
        mp_pool[i].join()

    print(result[:])
    return None

def main():
    supervisor()
    print(sum(1, 1000, 1))
    return None




if __name__ == "__main__":
    main()






