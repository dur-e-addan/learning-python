print("Aggregate Calulator")
#This takes input from the user
print("Enter your marks in below fields:")
matric = float(input("Enter your matric percentage:"))
fsc = float(input(" Enter your fsc percentage:"))
test = float(input("Enter your test percentage:"))
def aggregate_calculator(matric_score, fsc_score, test_score):
#Calculate their aggregate
    matric_score = matric_score * 0.1
    fsc_score = fsc_score * 0.4
    test_score = test_score * 0.5
    final_aggregate = matric_score + fsc_score + test_score
#Print their aggregate
    print("Your aggregate is:", final_aggregate)
#Print status
    if final_aggregate > 90.0:
        print("Congratulations! You secured a seat")
    elif final_aggregate >= 85.0 and final_aggregate <= 89.9:
        print("You have high chances for admission")
    else:
        print("Improve your score and try again")
aggregate_calculator(matric, fsc, test)
