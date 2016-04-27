#PEP8
class Person(object):
    #Class variable
    people_count=0
    def __init__(self,fname,age):
        # instance variable
        self.fname=fname
        self.age=age
        Person.people_count +=1

    def __repr__(self):
        return "<{}, {}>".format(self.fname, self.age)

    def say_hello(self):
        return "Hello am {} and i am {} years old".format(self.fname,self.age)


class Kenyan(Person):
    corrupt=False

    def probe(self,corrupt):
        self.corrupt=corrupt

    def is_corrupt(self):
        if self.corrupt:
            return "Yes"
        return "No"
