from person import Person

p = Person("Joey",23)
p1 = Person("Jane",14)
p2 = Person("Keem",14)


a=[("Jane",23),("Joe",33),("Jee",197),("Jacob",45),("Jacky",56)]


b=[]
for name,age in a:
    person=Person(name,age)
    b.append(person)

for people in b:
    print people.say_hello()

print p.say_hello()





#print Person.people_count

#print p.fname

#print p.age

#print p.people_count
