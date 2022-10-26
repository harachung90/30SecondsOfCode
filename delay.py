from time import sleep


def delay(fn, ms, *args):
    sleep(ms/1000)
    return fn(*args)


delay(lambda x: print(x), 1000, 'later') # prints 'later' after one second