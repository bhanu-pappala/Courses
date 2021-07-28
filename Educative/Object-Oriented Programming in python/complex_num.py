class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        temp = Com(self.real+other.real, self.imag+other.imag)
        return temp

    def __sub__(self, other):
        temp = Com(self.real-other.real, self.imag-other.imag)
        return temp

obj1 = Com(4,7)
obj2 = Com(9,2)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print(f'Real obj3 {obj3.real}')
print(f'Imag obj3 {obj3.imag}')
print(f'Real obj4 {obj4.real}')
print(f'Imag obj4 {obj4.imag}')
