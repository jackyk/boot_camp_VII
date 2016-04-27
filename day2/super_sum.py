def super_sum(A):
    '''
    Takes a list A and
        halves every even number,
        doubles every odd number
    #returns the sum of all,
    '''
    total = 0

    for x in A:
        if x % 2 == 0:
            total += (x / 2)
        else:
            total += (x * 2)

    return total

super_sum([2,3])
