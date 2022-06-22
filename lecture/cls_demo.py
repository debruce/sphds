class MyClass:
    '''This is my first class
    '''

    def __init__(self):
        self.x = 1
        self.y = 2

    def __repr__(self):
        return f'MyClass(x={self.x}, y={self.y})'

    def __iadd__(self, addend):
        self.x += addend
        self.y += addend
        return self

    def __getattr__(self, name):
        print(f'in __getattr__ with {name}')
        return 100

    def __setattr__(self, name, value):
        print(f'in __setattr__ with {name} {value}')

c = MyClass()


# help(c)
print(c.__doc__)

print(c.x)
print(c.y)

c += 55

print(c.x)
print(c.y)
print(c.hundred)

c.two_hundred = 200
print()

for item in [ 'x', 'y', 'hundred']:
    print(f'attr name={item} value={getattr(c, "x")}')
print()

setattr(c, "two_hundred", 300)