#WELCOME TO EMPLOYEE WAGE PROBLEM
'''
@Author: Chakravarthy

@Date: 2022-06-13 9:00:00

@Last Modified by: Chakravarthy

@Last Modified time: 2022-06-13 9:00:00

@Title : EMPLOYEE WAGE
'''
import random


EMP_RATE_PER_HR = 20
attendence =random.randint(0,1)
if attendence == 1:
    print("EMPLOYEE IS PRESENT")
    time_check = random.randint(1,2)
    if time_check == 2:
        salary = EMP_RATE_PER_HR * 8 # working hours of a employee in a day(full time) is 8
        print("EMPLOYEE IS PRESENT FULL TIME")
        print(f"SALARY OF AN EMPLOYEE IS {salary}")
    else:
        salary = EMP_RATE_PER_HR * 4 # working hours of a employee in a day(part time) is 4
        print("EMPLOYEE IS PRESENT PART TIME")
        print(f"SALARY OF AN EMPLOYEE IS {salary}")

else:
    print("EMPLOYEE IS ABSENT")
    salary = 0
    print(f"SALARY OF AN EMPLOYEE IS {salary}")
