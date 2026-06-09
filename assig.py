#string operations examples>>>>>>
name = "Anjali"

print(name[0])
print(name[-1])
print(len(name))
print(name.upper())
print(name.lower())
print(name[::-1])

# String slicing examples>>>>>>
text = "PythonProgramming"

print("First four characters:", text[:4])
print("Index 2 to 5:", text[2:6])
print("Reverse string:", text[::-1])


#list operations examples>>>>>>

numbers = [10, 20, 30, 40]

numbers.append(50)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.remove(30)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.reverse()
print("Reverse list:", numbers)

numbers.sort()
print("Sorted list:", numbers)

print("Length:", len(numbers))
print("Count of 20:", numbers.count(20))



sub = ("Python","DS","OOPS","SQL","AI")

print(sub[0])
print(sub[-1])
print(len(sub))
print(sub[1:4])

num = (10,20,30,40,50)

print(max(num))
print(min(num))
print(sum(num))



student = ("Anjali",20,"CSE","Python")

name,age,branch,course = student

print(name)
print(age)
print(branch)
print(course)




student = {
    "Name":"Anjali",
    "Age":20,
    "Course":"Btech",
    "Address":"Jaipur"
}

print(student.keys())
print(student.values())
print(student.items())

student["Address"]="Jaipur"

student["Branch"]="CSE"

print(student)



list1 = [1,2,3,4,[2,5],7]

print(list1[4][1])



num = int(input("Enter number: "))

num += 10

print(num)




a = input("Enter first number: ")
b = input("Enter second number: ")

a = int(a)
b = int(b)

print(a*b)



data = {
    "Name":"Anjali",
    "Age":20,
    "Course":"Btech"
}

print(data.get("Name"))

print(data.keys())

print(data.values())

print(data.items())




list1 = [10,20,30,40]

list2 = list1.copy()

print("Original list:", list1)

print("Copied list:", list2)

