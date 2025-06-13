# List:
        # A built in data type that stores set of values.
# It can store elements of different types (integer, float string etc..)

# marks = [95, 65, 68, 48, 88]

# student = ["Junaid", 24, "Multan"]

# student[0] = "Usama"

# len(student)

# print(marks)
# marks[0] = 99
# print(marks)


# List Methods

# list = ['a', 'b', 'c', 'd', 'e', 'f']
# list.append(4)  #add one element at the end
# print(list)


# list.sort()     # sort in ascending order
# print(list)

# list.sort(reverse=True)     # sort in descending order
# print(list)

# list.reverse()    # reverse list
# print(list)

# list.insert(0,'t')  # insert element at index
# print(list)


# list = [2, 1, 6, 1]
# list.remove(1)    # remove first occurence of an element
# print(list)

# list.pop(2)     #remove element at index 
# print(list)



                            # Tuples:

            # A built in data type that let us create immutable sequence of values.


# tup = (2,1,6,3,4)
# print(type(tup))
# print(tup[0])
# print(tup[1])

# tup[0] = 5  # not allowed in python



# Tuples Method.

# tup = (5,6,8,6,8)
# print(tup.index(6))     # return index of firts occurrence

# print(tup.count(6))     # counts total occurrence



# Practice

# Qs. WAP to ask the user to enter names of their 3 favourite movies & store them in a list.

# movies = []
# mov1 = input("Enter first movie name: ")
# mov2 = input("Enter second movie name: ")
# mov3 = input("Enter third movie name: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# Qs. WAP to check if a list contains a palindrome of elements.

# list = [1,2,3,2,1]

# copylist = list.copy()
# copylist.reverse()

# if(copylist == list):
#     print("The list is palandrome")
# else:
#     print("The list is not palandrome")



