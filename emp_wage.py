#WELCOME TO EMPLOYEE WAGE PROBLEM
'''@Author: Chakravarthy
@Date: 2022-06-13 9:00:00
@Last Modified by: Chakravarthy
@Last Modified time: 2022-06-13 9:00:00
@Title : EMPLOYEE WAGE
'''
import random


EMP_RATE_PER_HR = 20
attendence =random.randint(0,1)
if attendence == 1:
    salary = EMP_RATE_PER_HR * 8 # working hours of a employee in a day is 8
    print(f"EMPLOYEE IS PRESENT\nSALARY OF AN EMPLOYEE IS {salary}")
else:
     print("EMPLOYEE IS ABSENT")