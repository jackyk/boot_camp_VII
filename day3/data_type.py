def data_type(x):
    '''
    Its takes an argument,x:
    -For an integer, it and doubles it x**2
    -For a float, it returns x/2
    -For a string, returns "Hello"+ the string itself (x)
    -For a boolean, return type boolean
    -For a long return the sqrt of it
    '''
    if type(x) == int:
        return x ** 2

    elif type(x) == float:
        return x / 2

    elif type(x) == str:
        return (x) + (x)

    elif type(x) == bool:
        return "boolean"

    elif type(x) == long:
        return "long"

    else:
        print "Something is not right"

print data_type(2)
print data_type(4.0)
print data_type("Day3 ")
print data_type(True)
print data_type(25 ** 255)
