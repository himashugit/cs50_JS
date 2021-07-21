people = [
    {"name":"himanshu", "house":"ardwick"},
    {"name":"geeti", "house":"songwood"},
    {"name":"hermione", "house":"delta"}

]

#def f(person):
 #   return person["house"] # defining a function which store the  value and return it by using sort method.



#people.sort(key=f)
people.sort(key=lambda person: person["name"]) # instead you can use the lambda func to get the same result

print(people)

