import itertools
import asyncio



async def spin(msg):  # <1>
    for char in itertools.cycle('|/-\\'):  # <3>
        status = char + ' ' + msg
        print(status, flush=True, end='\r')

        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

    print(' ' * len(status), end='\r')




async def slow_function():  # <7>
    # pretend waiting a long time for I/O
    await asyncio.sleep(3)  # <8>
    return 42


async def supervisor():
    spinner = asyncio.create_task(spin('Thinking!!'))
    print('spinner object:', spinner)
    result = await slow_function()
    spinner.cancel()
    return result




def main():
    result = asyncio.run(supervisor())  # <15>
    print('Answer:', result)



if  __name__ == '__main__':
    main()
