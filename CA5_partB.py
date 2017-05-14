#CA5 part B - involves modifying your calculator class from CA1 to ensure that it can handle lists of data.
#You will be required to refactor / rewrite your functions so that they can handle lists.
#You will need to use lambda, map, filter, reduce and list comprehension in any manner you deem necessary to achieve this.

#max function
def max(a,b):
    if a>b:
        return a
    return b
f = lambda a,b: a if (a>b) else b

print reduce(f, [47, 11, 42, 13])

#print reduce(lambda x, y: x+y, range(1, 101))

#SUM
def sum(values):
    return reduce(lambda x, y: x+y, values)

#ADD
add = lambda x,y: x+y

#MAX
def max(values):
    return reduce(lambda a,b: a if(a>b) else b, values)

#MIN
def min(values):
    return reduce(lambda a,b: a if (a<b) else b, values)

#ADD
def add(first, second):
    return map(lambda x, y: x+y, first, second)

#DIVIDE
def divide(first, second):
    return map(lambda x, y: x/float(y) if y!=0 else 'nan', first,second)

#IS EVEN
def is_even(values):
    return filter(lambda x: x%2==0, values)

#greater than mean
def greater_than_mean(values,mean):
    return filter(lambda x: x>mean, values)

#celsius to fahrenheit
def to_fahrenheit(values):
    return [((float(9)/5)*x + 32) for x in values]

print sum([47,11,42,13])
print max([47,11,42,13])
print min([47,11,42,13])
print add([47,11,42,13], [37,21,22,33])
print divide([9,16,4], [1,4,0])
print is_even([47,11,42,13])
print greater_than_mean([47,11,42,13], 28.25)

#celsius, fahrenheit calculator
def fahrenheit(t):
    return ((float(9)/5)*t + 32)
def celsius(t):
    return (float(5)/9*(t - 32))
temp = (36.5, 37, 37.5, 39)

F = map(fahrenheit, temp)
print F
C = map(celsius, F)
print C

fib = [0,1,1,2,3,5,8,13,21,34,55]
print fib
result = filter(lambda x: x % 2 ==0, fib)
print result

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print Fahrenheit

Fahrenheit = to_fahrenheit(Celsius)
print Fahrenheit

#coloured things
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print coloured_things

coloured_things = []
for x in colours:
    for y in things:
        coloured_things.append((x,y))
print coloured_things

#generator
def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
    
x = city_generator()
print x.next()
print 'Hello'
print x.next()

#fibonacci
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a = 0
    b = 1
    counter = 0
    while True:
        if (counter > n): return
        print 'hi',
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5)

print f.next()


