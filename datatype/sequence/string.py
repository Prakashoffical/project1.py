# string : sequence of charactor that is enclosed with single,duble,triple quotation.(' '' ''') 
#a='prakash said,"i want to learn python"'
#print(a,type(a))

#a="prakash"
#print(len(a)) #lenth of character 

#   index, slice 
#   index: the way of accessing element by there position 
#a="prakash" #01234567...../ space also cound 
#print(a[5])
#a="prakash"
#print(a[-6])
#              slicing: the way of accessing of element by thier position 
#     syntax: variable_name[start:end:step]

#a="my name is prakash" #need to print name (count number 0123456789.....)
#print(a[3:7:1]) #in the last latter :1 is not necessary at's inbild auto if move more then 1 when count word then we can use.
#print(a[3:7])
#if we need name is :
# print(a[3:10])


#function & method 
#function()
#a.method ()

# a="I Am Prakash"
# string method :47 method

#print(len(a))    #it's count the numer of latter
#print(a.lower())   #its make all latter small 
#print(a.upper())   #it's make all capital latter
#print(a.swapcase())  #it will make capital to small and small to capital latter 
#print(a.title())    #it will make every first latter capital
#print(a.capitalize())   #it make first latter capital 
#print(a.casefold())  #it work same lower but it work force fully  if lower comand not work use it (aggressive)
#print(a.startswith("my")) #--it user for true and false if latter stary from "my" shows true (and its case sencative )
#print(a.endswith(h))  #it's show last latter (h) true & false 
#print(a.islower())  #if lattrer is small it shoe true nither false
#print(a.isalnum())  #in this command show if any alfabet or numarical world its show TRUE

#print(a.replace("Prakash","ayush")) #it's help to change world,latter and sentence 
# print(a.index("P")) #is how index number of latter 
#print(a.count("a"))  #it's help to COUNT how manny same namber and name in pragraf 



#sentence : user word---->count()
#sentence='''Python is a popular and easy programming language.
#It is used to make websites, games, and applications.
#Python is also used for AI, data science, and automation.
#It has simple syntax, so beginners can learn it easily.
#Python is a powerful and useful language for many projects.'''

#user="is"
#user=input("Enter your word to count : ")

#print(sentence.count(user))

#case sencitive (lower) or (upper)
#print(sentence.lower().count(user))

 

#raw data------>clean date----->analyze data---->pattern (findout)----->(predict)
 
#          split and strip :for data clining 

#                          split 

# a="my name is prakash"
#email="prakashbishwakarma19@gmail.com"
# print(a.split())
# print(a.split(a))
#print(email.split("@"))

#password="prakash"

#a="   welcome  "
#print(a.strip())

#b="!!!welcoome!!!"
#print(b.strip("!"))
#print(b.lstrip("!"))
#print(b.rstrip("!"))

#name="prakash1999"
#print(name.strip("123456789"))

# #domain="www.facebook.com"
# domain=input("enter your domin name : ")
# print(domain.lstrip("w.").rstrip(".com"))
# ------> mustly we use. for data clining.
# print(domain.removeprefix("www.").removesuffix(".com"))
# ----> thats remove exat what we give to remove 

# 