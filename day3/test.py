other_people=[
    ("Joey",78),
    ("Jik",78),
    ("Joyt",78)
    ]
'''
def super_sum(*args):
    return sum(args)
'''
def hello_again(name,age):
    return "I am {} and {} years old".format(name, age)

def max_min(A):
'''Returns the max value - min value'''

    max_ , min_ = A[0], A[0]

    for i in A:
        if i > max_:
            max_ = i
        elif i < min_:
            min_= i

    return max_ - min_
