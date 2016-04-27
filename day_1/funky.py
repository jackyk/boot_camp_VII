
def make(a,b):
    if type(a) and type(b) == (str):
        return (a+b)
    elif type(a) is float and type(b) is int or  type(a)is int and type(b) is float:
        return sum([a,b])
    elif type(a) and type(b) == (list):
        return (a+b)
    elif type(a) and type(b) ==(dict):
        return dict.keys()
    else:
        return "MY CODE IS NOT WORKING STILL WORKING ON IT"


make ("ha","ppy")
make(2,3.2)
print make("ddf",1)
