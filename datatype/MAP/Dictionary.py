
# #Dictionary:  
# 
# ---->  collection of data items (data structure) that have key-value pair which is mutable, order (verson 3.7)
# #do not allow duplicate.dictionary Represent {}
# '''
# a={ 
#  "name":"prakash",   # key : name / value: prakash 
#    "age":27  
#   }



# #print(len(a))
# #print(a(0))

# #print(a["age"])
# #print(a.get("age"))

#  #print(a["age"]) #it show errer 
#  #print(a.get("email","not found")) #it's show none or we can add not found (any word)

#        ADD NEW VALUE    

# a={
#  "name":"prakash", # key : name / value: prakash 
#    "age":27  
#   } 

# # a["email"]="prakash9@gmail.com"

# b={
#     "age":99,
#     "address" : "nepal"
# }
# a.update(b)

# a.pop("name") #pop help to remove value from data
# a.popitems()# popitems: it's help to remove last value
# a.clear() #it's clear all data from a 
# del a #it's delect all data from A

# a.setdefault("name","manoj") # Use: Adds a value to a dictionary only if the key does not already exist

# print(a)
# a={ 
#     "username":"prakash",
#     'password':'19987'

# }

# username=a['username']
# pw=a.get("password","not found")

# print(a)

#             NESTED DICTINARY
# : one dictinary inside another dectinary:
# marks={
#     "roll no 1":{
#         "name":"sujan",
#         "grade":"A"
#        },
#         "roll no 2 ":{
#         "name":"rohan",
#         "grade":"B"
#         }
# }
# roll1=marks["roll no 1"]  #{"name":"sujan", "grade":"A"}

# print(type(roll1))
# print(roll1["name"])

# that command on one line :

# print(marks["roll no 1"]["name"])
# print(marks["roll no 2 "]["grade"])


# marks["roll no 1"]['name']='prakash' #="value" it's help to change value(update new value )"
# print(marks)    



      #     TASK 1

#given to dictionary person={'name':'sujan','age':29,'city':'pokhara'},
# add the new key value pair 'jobe': 'developer' to the dictionary.
# then update value of the 'name' key to 'ram bahadur' and 'age' to 45.

# person={
#       'name':'sujan',
#         'age':29,
#         'city': 'pokhara'    
# }

# print(person.values()) #that command only show valuw of key.
# print(person.key())
# print(person.items()) #it bring keys and value all.
# person["job"]="devloper" #this command add data direct on person.
# b={
#     'name':'ram bahadur',
#     'age':45
# }
# person.update(b)
# print(person)

