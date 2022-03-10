def doubler(func):
    def inner():
        func()
        func()
    return inner

@doubler
def test():
    print("HI")

test()