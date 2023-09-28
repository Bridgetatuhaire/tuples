#working with tuples
#accessing tuple items

marks = (80, 79, 69, 70)
marks[0]
print(type(marks))
print(marks[0]) 

#tuples with single int must add a ,
marks=(80,)
print(marks)
#when the int has no , it will be a dictionary
marks=(80)
print(marks)

#check whether 79 exists in the variable marks ,print {79 is a member of variable marks}
#check whether 89 does exist if not print item/value does not exist

marks = (80, 79, 69, 70)
if 79 in marks:
    print("79 exists in the variable marks")
else: #caters for the items that are not in the tuple
    print("79 does not exist")
print('89 doesnot exist in the variable marks')


#string interpolation
age = 25
name = "Bridget"
print(f"My name is {name} and I am {age} years old.")

#for else statements

teenager = 1-18
youth = 19-29
if (age<=1 and age>=18):
    print('teenager')
else:
    (age>=19 and age<=29)
    print('youth')

#modification of the tuples

marks = (60,79,69,70)

#changing a tuple to the list
new_marks = list(marks)
print(type(new_marks), new_marks)

new_marks[1] = 88
print(tuple(new_marks)) #converting the new list into a tuple

#adding 99 to the tuple
updated_marks = tuple(new_marks)
updated_list_marks = list(updated_marks)
updated_list_marks.append(99)
print(tuple(updated_list_marks))