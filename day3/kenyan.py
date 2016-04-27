from person import Person
from person import Kenyan


k= Kenyan('Anita Waiguru',29)

k.probe(True)

print "Is {} corrupt {}".format(k.fname, k.is_corrupt())

print k.say_hello()
