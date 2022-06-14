#WELCOME TO EMPLOYEE WAGE PROBLEM
'''
@Author: Chakravarthy
@Date: 2022-06-13 9:00:00
@Last Modified by: Chakravarthy
@Last Modified time: 2022-06-13 9:00:00
@Title : EMPLOYEE WAGE
'''
# Importing random modules

import random


WAGE_PER_HOUR = 20
emp_work_hour = 0
emp_daily_wage = 0
total_month_wage = 0


# Checking that employee is present for full time , part-time or absent
def present_for_fullTime():
    """
        Description:
            This function is set employee work hours as 8 for full time presence of employee
        Parameter:
            None
        Return:
            Employee Work Hours
    """
    emp_work_hour = 8
    return emp_work_hour


def present_for_partTime():
    """
        Description:
            This function is set employee work hours as 4 for part-time presence of employee
        Parameter:
            None
        Return:
            Employee Work Hours
    """
    emp_work_hour = 4
    return emp_work_hour


def absent():
    """
        Description:
            This function is set employee work hours as 0 for absence of employee
        Parameter:
            None
        Return:
            Employee Work Hours
    """
    emp_work_hour = 0
    return emp_work_hour


def switch_case(check):
    """
        Description:
            This function is used for implementing switch case for employee attendence
        Parameter:
            This function takes one integer parameter
        Return:
            It returns function value based on choice
    """
    switcher = {
        0: absent(),
        1: present_for_partTime(),
        2: present_for_fullTime(),  
    }
    return switcher.get(check, "")


if __name__ == "__main__":
    for day in range(20):
        check = random.randint(0, 2)
        result = switch_case(check)  
        emp_daily_wage = result * WAGE_PER_HOUR
        total_month_wage += emp_daily_wage  # Adding daily wage to total wages
    print(f"Employee total month wage for 20 days is : {total_month_wage}")
