

a = 1234
def test(b):
    print(b is a)
    b='hello'
    print(b is a)

test(a)