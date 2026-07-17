subjects = []
marks = []
while True:

    try:
        number_sub = int(input("Enter the number of subjects you took:"))
        break
    except ValueError:
        print("Please enter a valid number.")
for i in range(number_sub):
    user_sub = str(input("Enter the name of subject:"))
    subjects.append(user_sub)
    while True:
        try:
            user_marks = int(input("Enter marks obtained out of 100:"))
        except ValueError:
            print("Enter a valid number.")
            continue
        if user_marks > 100 or user_marks < 1:
            print("Marks must be between 0 and 100")
        else:
            marks.append(user_marks)
            break
for i in range(number_sub):
    print(f'{subjects[i]} : {marks[i]}')
total_marks = sum(marks)
average_marks = total_marks/number_sub
if average_marks < 50:
    print("You've Failed successfully!")
else:
    print("Unexpectedly, You've Passed!")
