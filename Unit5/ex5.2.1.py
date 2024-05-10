a = 1

def foo1():
    print(a)

foo1()
print(a) # 1 and then 1

b = 1

def foo2():
    b = 2
    print(b)
  
foo2()
print(b) # 2 and then 1

c = 1

def foo3():
    c = c + 1
    print(c)

foo3()
print(c) # error

d = 1

def foo4():
    global d
    d = 2
    print(d)

foo4()
print(d) # 2 and then 2