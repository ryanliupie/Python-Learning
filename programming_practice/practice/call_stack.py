# The Call Stack 

def a():
    print('a() starts')
    b()
    d()
    print ('a() returns')

def b():
    print('b() starts')
    c()
    print(('b() returns'))

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

# we call a() and it prints out 'a() starts'
# a() calls b() so b() is added to the call stack which would print 'b() starts'

# now we might think that a() should call d() right? No lol. Since a() calls b(), we have to finish what is in b() because it gets push onto the stack which must be completed before we can do another function

# b() calls c() so c() is added to the stack and prints 'c() starts' and 'c() returns'
# now in c() it does not call any other function, so we are going to go back to a()
# in a() it calls function d() and prints out 'd() starts' and 'd() returns'
# in d() it does not go to any other function so we are going to go back to a() and see what is next yet again
# the last thing that gets printed out would be 'a() returns'