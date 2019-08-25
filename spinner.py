import itertools
import threading
import time



def spin(msg, done) -> None:  # <1>
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
    for _ in range(10000):
        done = threading.Event()
        spinner = threading.Thread(target=spin, args=('Thinking!!', done))
    print('Spinner Object', spinner)
    spinner.start()
    result = slow_function()
    done.set()
    spinner.join()
    return result




def main():
    result = supervisor()  # <15>
    print('Answer:', result)



if  __name__ == '__main__':
    main()
