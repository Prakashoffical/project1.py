# loop :- A loop repeats code until a condition is met
# the loop is programing structure that repeat block of code multiple time base on condition or number of iteration.


# type  of loop:-  1) for loop :-it is use for repeat predetermine number
#                  2)while loop:-

# 1).for loop :- A for loop automatically repeats code for each item in a "list, string, tuple, set or range" until all items are processed)
    # syntax:
'''
for item in iterable:
    block of code                
'''
# a=[1,2,3,4]
# print(4 in a) #(in  :_ is memmbership oprater )(a ma 4 xa vanera qtn)

#                  list
# name=["prakash","rewa","sujan","ujjwal","rita"]
# for i in name:
#     print("hi welcome",i) #i repert every name on this command

#                 string
# name="prakash"
# for i in name:
#     print(i)

#    Map              {dictionary} def,inpot..

# a={
#    "name":"prakash",
#    "age":21,
#    "home":"austrila"

# }

# for i,j in a.items(): 
#     print(i,j)

#                         Rang

#   syntax :-- rang(start,end,step)

# for i in range(0,1000,1):  #1,2,3,4,5,6,7,8,9
#     print(i,"prakash")#for just print number , print(i) and add any word if wants

#5,4,3,2,1
# for i in range(5,0,-1):
#     print(i)

#  multiplication
'''2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20'''

# num=int(input("enter your multiplication nim:- "))
# # num=2
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)