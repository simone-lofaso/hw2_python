import time

def calculate_time(func):
    def inner():
        startTime = time.time()
        func()
        endTime = time.time()
        print("Total time", endTime - startTime)
    return inner()

@calculate_time
def test():
    time.sleep(2)
    print(6)