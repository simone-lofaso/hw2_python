import time

def calculate_time(func):
    def inner():
        startTime = time.time()
        func()
        endTime = time.time()
        print("Total time", endTime - startTime)
    return inner

def test():
    return

test = calculate_time(test)

test()