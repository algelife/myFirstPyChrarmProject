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
def spin(msg, done, thread_number) -> None:  # <1>
    print('thread_number: ', thread_number)
    for char in itertools.cycle('|/-\\'):  # <3>
        status = char + ' ' + msg
        print(status, flush=True, end='\r')
        if done.wait(.1):  # <5>
            break
    print(' ' * len(status), end='\r')

def slow_function():  # <7>
    # pretend waiting a long time for I/O
    #for _ in range(10):
    time.sleep(3)  # <8>
    return 42



def supervisor():
    done = threading.Event()
    spinner = []
    for i in range(10):
        spinner.append(spin("thinking!!", done, i))
        #time.sleep(1)

    result = slow_function()
    done.set()
    [spinner[i].join() for i in range(10)]
    return result

def main():
    result = supervisor()  # <15>
    print('Answer:', result)


if  __name__ == '__main__':
    main()
