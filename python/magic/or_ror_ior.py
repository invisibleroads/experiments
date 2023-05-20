class X:

    def __ior__(self, _):
        print('__ior__', self, _)

    def __or__(self, _):
        print('__or__', self, _)

    def __ror__(self, _):
        print('__ror__', self, _)


x = X()
x | 1
1 | x
x |= 1
