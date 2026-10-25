'''conditional statemnt: '''

# name=input("enter your name : ")
# marks=int(input("enter your marks : "))

# if marks>45:
#     print(f"hi {name} \nresult = pass")
# else:
#     print(f"hi {name} \nresult = fail")


'''for loop statement '''

# for i in range(5):
#     name=(input("enter name : "))
#     marks=int(input("inter marks : "))

#     if marks>45:
#         print(name,"psss")

#     else:
#         print(name,"fail")

""" conditional example 2 """

# name="prakash"

# if name.startswith("p"):
#     print("yes")
# else:
#     print("no")


'''for loop  and use of " op "  example'''

# name=["prakash","pramesh","sujan","roshni","puja"]
# op=[ ] #it store file which in store op
# for i in name:
#     if i.startswith("p"):
#         print(i)
# print(op)

# marks=[23,45,56,12,12,78,90]
# op=[]
# for i in marks:
#     if i>50:
#         op.append(i)
# print(op)


'''example 3'''
# marks=[12,18,43,13,50,58,42,46,68]

# for i in marks:
#     if i>45:
#         print(i)

'''example 4'''
# age_group=[17,13,88,34,40,20]
# op=[]
# for i in age_group:
#     if i>18:
#         op.append(i) #append() adds one item to the end of a list.
# print(op)

'''example 5'''
# num=[12,13,11,3,5,2,4]
# op=[]
# for i in num:
#     if i % 2 ==0:
#         op.append(i)
# print(op)


''' nested loop : one loop inside another loop'''
name=["prakash","sujan","pramesh"]
for i in name:
    print(i)
    for j in i:
        print(j)