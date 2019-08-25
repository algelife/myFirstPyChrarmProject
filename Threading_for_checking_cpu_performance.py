import threading
import itertools
import time



def run_async(func):
	"""
		run_async(func)
			function decorator, intended to make "func" run in a separate
			thread (asynchronously).
			Returns the created Thread object

			E.g.:
			@run_async
			def task1():
				do_something

			@run_async
			def task2():
				do_something_too

			t1 = task1()
			t2 = task2()
			...
			t1.join()
			t2.join()
	"""
	from threading import Thread
	from functools import wraps

	@wraps(func)
	def async_func(*args, **kwargs):
		func_hl = Thread(target = func, args = args, kwargs = kwargs)
		func_hl.start()
		return func_hl

	return async_func


@run_async
def sum(a, b, thread_number):
    print("thread_num", thread_number)
    s=0
    for i  in range(a, b+1):
        s+=i
    print(s)
    return s



def supervisor():
    thr = []
    for i in range(10):
        thr.append(sum(1, 10000000, i))

    for i in range(10):
        thr[i].join()

    return None

def main():
    supervisor()
    return None


if __name__ == "__main__":
    main()






