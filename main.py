from aritmetic_module.aritmetic_operations import *

if __name__ == '__main__':
    print(four(times(five()))) # print 20
    print(one(plus(eight()))) # print 9
    print(seven(minus(three()))) # print 4
    print(nine(divided_by(three()))) # print 3
    print(three(minus(nine()))) # print -6
    print(four(times(five(plus(five()))))) # print 60
    # The big one
    print(four(times(five(times(four(plus(eight(minus(nine()))))))))) # print 60