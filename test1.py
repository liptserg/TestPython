#test


def test():
    print('from module main.py __name__ ==', __name__)
    return '\n Hello!'

def qwe():
    print(2 **10)
    test()

qwe()
