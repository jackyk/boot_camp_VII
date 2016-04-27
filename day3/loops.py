'''a=[1,2,3,4,5,6,7]

for i in a:
    print i
    #print your list

i=len(a)

while i > 0 :
    print a[i -1]
    i -=1

for x in range(i -1, -1, -1):
    print a[x]
'''

b=[(2,3),(1,4),(8,9),(8,0)]

'''
create a table x,| y
                2|3'''

for i in b:
    #print i
    print "x:{} | y:{}".format(*i)
