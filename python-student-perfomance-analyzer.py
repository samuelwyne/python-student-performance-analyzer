students=[]
while True:
  try:
    num=int(input("Enter number of students: "))
    if num>0:
      break
  except ValueError:
      print("Try agin!")
for i in range(num):
  student={}
  student["name"]=input("Enter student's name: ")
  student["course"]=input("Enter student's course: ")
  while True:
    try:
     student["mark"]=int(input("Enter student's marks: "))
     if student["mark"]>0 and student["mark"]<101:
       break
    except ValueError:
      print("invalid marks try agin!")
  students.append(student)
  print()  

while True:
 status=input("Do yo want to arrange them in ascending or descending?(A/D)\n")
 if status.upper()=="A":
    ordered=sorted(students,key=lambda student:student["mark"])
    print(f"{'Name':15}{'Course':20}{'Marks':8}")
    for student in ordered:
     print(f"{student['name']:15}{student['course']:20}{student['mark']:8}")
    break
 elif status.upper()=="D":
    ordered=sorted(students,key=lambda student:student["mark"], reverse=True) 
    print(f"{'Name':15}{'Course':20}{'Marks':8}")
    for student in ordered:
     print(f"{student['name']:15}{student['course']:20}{student['mark']:8}")
    break
 else:
     print(" invalid choice! Try again:") 
 
highest_student=max(students,key=lambda student: student["mark"])
lowest_student=min(students,key=lambda student: student["mark"])
print()
print("\nHishest Student")
print(f"Name   : {highest_student['name']}")
print(f"Course : {highest_student['course']}")
print(f"Marks  : {highest_student['mark']}")
print()
print("\nLowest Student")
print(f"Name   : {lowest_student['name']}")
print(f"Course : {lowest_student['course']}")
print(f"Marks  : {lowest_student['mark']}")

print()
print(f"{"="*5}PASSED STUDENTS{"="*5}")
passed_students = list(filter(lambda student: student["mark"] >= 50, students))
for student in passed_students:
    print(f"{student['name']} - {student['mark']}")