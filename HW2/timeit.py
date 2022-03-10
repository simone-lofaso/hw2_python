import time

def calculate_time(func):
    startTime = time.time()
    func()
    endTime = time.time()
    print("Total time", endTime - startTime)

@calculate_time
def test():
    time.sleep(2)
    print(6)