
def super_sum(*args):
    '''
    Takes in a va of items and return the super_sum
    super_sum(1,2,3,4,5)
    super_sum(44,5,6,7,9)
    '''
    total=0
    for i in args:
        total+= i
    return total

print super_sum(10,20)
print super_sum(1,4,5,7)
'''a,b,c=[(1,2,3),(4,5,6),(7,8,9)]
print super_sum(*a,*b,*c)'''




def hello_again(**kwargs):
    return "My name is {} ,and I am this {} years old".format(kwargs['name'],kwargs['age'])

    #print hello_again(name="Joe", age=20)
other_people=[
    {"name":"Joey","age":78},
    {"name":"Jik","age":78},
    {"name":"Joyt","age":78},
    ]
#for persons in other_people:

Joe={"name":"Joey","age":78}

print hello_again(**Joe)
