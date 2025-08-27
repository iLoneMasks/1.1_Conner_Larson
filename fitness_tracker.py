'''
    author: Conner Larson-Snow
    date: 25/08/25
    version: 1
    description: This code is to collect data from the user and store the values in a list
'''
#--------libraries---------------
import random
#--------functions---------------
def main():
    name = ''
    age = ''
    run_times_list = []
    run_times_inputs = 5

    name = input('What is your name?: ')
    name.append(name)
    while True:
        try:
            age = int(input('How old are you?: '))
            if age > 13
            break
        else:
            print("Your age is invalid.")
    age.append(age)
    for i in range(run_times_inputs):
        run_times = input(f"Please enter your run time: ")
        run_times_list.append(run_times)
#-----main-----------------------
if(__name__== "__main__"):
    main()