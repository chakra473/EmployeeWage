# WELCOME TO EMPLOYEE WAGE PROBLEM
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
total_emp_work_hour = 0
emp_daily_wage = 0
total_month_wage = 0


def get_work_hours(check):
    """ 
        Description: 
            This function is calculating workhours based on employee attendence
        Parameter:
            It takes one integer as argument
        Return:
            returns employee work hours for one day 
    """
    if check == 1:
        emp_work_hour = 4
    elif check == 2:
        emp_work_hour = 8
    else:
        emp_work_hour = 0
    return emp_work_hour


if __name__ == "__main__":
    day = 1
    working_days = 0
    daily_wage_dict = {}
    while day <= 20 and total_emp_work_hour <= 100:  # no of working days is 20 and maximum working hours is 100
        check = random.randint(0, 2)
        result = get_work_hours(check)
        if result != 0:
            emp_daily_wage = result * WAGE_PER_HOUR
            daily_wage_dict[day] = emp_daily_wage
            total_emp_work_hour += result
            total_month_wage += emp_daily_wage  # Adding daily wage to total wages
            day += 1
            working_days+=1
        else:
            daily_wage_dict[day] = 0
            day += 1
    if total_emp_work_hour > 100:  # Checking that hours are more than 100 or not
        extra_hours = total_emp_work_hour - 100
        total_emp_work_hour -= extra_hours
        wage = extra_hours * total_emp_work_hour  # Calculate extra hours wage
        total_month_wage -= wage  # Minus extra hours wage from emp total wage
        print(f"Extra hours that employee worked {extra_hours}")# Minus extra hours wage from emp total wage
    print(" Day  : DailyWage")
    for i in sorted(daily_wage_dict):  # sorting dictionary by key
        print(f"Day {i} : {daily_wage_dict[i]}")
    print(f"EMPLOYEE TOTAL WAGE IS {total_month_wage}")
    print(f"TOTAL WORKING HOURS OF THE EMPLOYEE IS {total_emp_work_hour}")
    print(f"TOTAL WORKING DAYS OF THE EMPLOYEE IS {working_days}")
