'''def hello(name ,age):
    '''
    This is what I want to do
    UNPACKING
    '''
    return "I am {} and I am {} y/old".format(name,age)

    people=[("Jane",23),("Joe",25),("Brian",60),("Betty",45)] #list of tuples

    for name,age in people:
        print hello(name,age)

for person in people:
    print hello(*persons)'''

def super_sum(*args)
    '''
    Takes in a va of items and return the super_sum
    super_sum(1,2,3,4,5)
    super_sum(44,5,6,7,9)
    '''
    total=0
    for i in args:
        total+= i
