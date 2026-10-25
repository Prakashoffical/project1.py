# set : collecation of data items(data structture) whice is 
# 1. mutable (mutable : we can change value of it. )
# 2. unorder 
# 3. do not allow dublicate 

#    use like math set sub : see on net
 
# it's represent by : {}
# a={"prakash",1,2,3,"ram","ram","ram","prabin"}

# print(type(a))
# print(a)
##  print(a[0]) or print(a[0:3]) :----> this cmd does not work in set (index slice only wort on sequence)

# a.add("krishna") #add : we can add data
# a.update({'manoj',1,5,7,'prabin',2}) # update :we can add multy data .
# a.remove("prabin")
# a.discared("prakash")  : it's help to remove and if we dont have data dosen't show ERRER

# print(a)

#                     set meth solve
# a={1,2,3,4,5}
# b={2,4,6,8}

# c=a.intersection(b)
# c=a.union(b)
# c=a.difference(b)  #work as like simmelar like (a-b)
# c=a.difference(a)
# c=a.symmetric_difference(b)


print(c)


# old_emp={"sujan","himal","manoj","hari"}
# new_emp={"sujan","milan","suyog","rajan","rohan"}

# print(old_emp.difference(new_emp))

#      frozenset : immutable
# a=frozenset{1,2,3,4,5}
# b={2,4,6,8}

# a.intersection_update(b)
# a.add(99)   #:after use froz its not work.
# print(a)
