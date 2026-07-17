subjects = []
marks = []
number_sub = int(input("Enter the number of subjects you took:"))
for i in range(number_sub):
     user_sub = str(input("Enter the name of subject:"))
     subjects.append(user_sub)
     user_marks = int(input("Enter marks obtained out of 100:"))
     marks.append(user_marks)
for i in range(number_sub):
    print(f'{subjects[i]} : {marks[i]}')
total_marks = sum(marks)
average_marks = total_marks/number_sub
if average_marks < 50:
    print("You've Failed successfully!")
else:
    print("Unexpectedly, You've Passed!")
