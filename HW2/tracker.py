def func_counter(func):
    
    def count(*arg):
        count.counter += 1
        func(*arg)
    count.counter = 0
    return count    
    
@func_counter
def test(y):
    print(y)

test(4)
test(4)
test(4)
print(test.counter)