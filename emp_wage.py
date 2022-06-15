#WELCOME TO EMPLOYEE WAGE PROBLEM
'''
@Author: Chakravarthy
@Date: 2022-06-13 9:00:00
@Last Modified by: Chakravarthy
@Last Modified time: 2022-06-13 9:00:00
@Title :python code for calculating EMPLOYEE WAGE
'''
# Importing random modules

import random


WAGE_PER_HOUR = 20
total_emp_work_hour = 0
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
    return switcher.get(check)


if __name__ == "__main__":
    day = 0
    working_day=0
    while day < 20 and total_emp_work_hour <= 100:   #no of working days is 20 and maximum working hours is 100
        check = random.randint(0, 2)
        result = switch_case(check) 
        if result != 0:
            emp_daily_wage = result * WAGE_PER_HOUR
            total_emp_work_hour +=result
            total_month_wage += emp_daily_wage  # Adding daily wage to total wages
            day+=1
            working_day+=1
        else:
            day+=1
    if total_emp_work_hour > 100:  # Checking that hours are more than 100 or not
        extra_hours = total_emp_work_hour - 100
        total_emp_work_hour -= extra_hours
        wage = extra_hours * total_emp_work_hour  # Calculate extra hours wage
        total_month_wage -= wage
    print(f"EMPLOYEE TOTAL WAGE IS {total_month_wage}")
    print(f"TOTAL WORKING HOURS OF THE EMPLOYEE IS {total_emp_work_hour}")
    print(f"TOTAL WORKING DAYS OF THE EMPLOYEE IS {working_day}")
