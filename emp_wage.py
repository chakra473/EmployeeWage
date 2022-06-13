#WELCOME TO EMPLOYEE WAGE PROBLEM
'''
@Author: Chakravarthy

@Date: 2022-06-13 9:00:00

@Last Modified by: Chakravarthy

@Last Modified time: 2022-06-13 9:00:00

@Title : EMPLOYEE WAGE
'''
import random


PRESENT = 1
ABSENT = 0
def  employee_attendence():
    """
    Description:
        This method checks whether employee is present or absent
    Parameter:
        None
    Return:
        Returns string
    """
    attendence =random.randrange(0,2)
    if attendence == PRESENT:
        return "EMPLOYEE IS PRESENT"
    else:
        return "EMPLOYEE IS ABSENT"


if __name__ =="__main__":
    print(employee_attendence())
