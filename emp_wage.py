#WELCOME TO EMPLOYEE WAGE PROBLEM
'''@Author: Chakravarthy
@Date: 2022-06-13 9:00:00
@Last Modified by: Chakravarthy
@Last Modified time: 2022-06-13 9:00:00
@Title : EMPLOYEE WAGE
'''
import random


EMP_RATE_PER_HR = 20
def daily_wage_switch_case(argument):
    switcher = {
        1: f"EMPLOYEE IS PRESENT PART TIME\nSALARY OF THE EMPLOYEE IS {4 * EMP_RATE_PER_HR}",
        2: f"EMPLOYEE IS PRESENT FULL TIME\nSALARY OF THE EMPLOYEE IS {8 * EMP_RATE_PER_HR}",
    }
    return switcher.get(argument, "EMPLOYEE IS ABSENT")


if __name__ == "__main__":
    attendence = random.randint(0, 2)
    print((daily_wage_switch_case(attendence)))