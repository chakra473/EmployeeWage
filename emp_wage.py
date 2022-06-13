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


def daily_wage():
    """
    Description:
        This method calculates daily wage of the employee
    Parameter:
        None
    Return:
        Returns salary in number(int)
    """
    attendence=random.randrange(0,2)
    if attendence == PRESENT:
        emp_rate_per_hr = 20
        emp_hrs = 8
        salary = emp_rate_per_hr * emp_hrs
        return salary
    else:
        salary = 0
        return salary


if __name__ =="__main__":
    print(employee_attendence())
    print(daily_wage())
