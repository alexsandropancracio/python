def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return
        
def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen):
    yield from gen1()
    yield 4
    yield 5
    yield 6
        
g = gen2(gen1())

for numero in g:
    print(numero)

print()

gen = generator(n=0, maximum=10)

for x in gen:
    print(x)
