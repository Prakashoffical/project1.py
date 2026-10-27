# loop control statement : it is used to change flow of excutation, skip, stop the excutation

# 1) pass
# 2) break
# 3) continue
# 4) else

#pass : it is null statement which is use for future code 
# for i in range(10):
    # pass


#break: it is use terminate loop whien encounter

# for i in range(1,10):
#     if i==5:
#         print("5 found")
#         break  #this command stop when 5 found
#     print(i)


# continue : it is used to stop current iteration and skip to next iteration

# for i in range(1,10):
#     if i%3==0:
#         continue #it's break the code when 3 found and countinue another code
#     print(i)#1,2,3,4


#else:    

a=[2,1,3,4,0,5,6] # if we add zero

for i in a:
    # print(i)
    if i == 0:
        print("zero is found!!!")
        break

else:
    print("zero is not available. loop end")