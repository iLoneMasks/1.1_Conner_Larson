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
    run_times = []

    name = input('What is your name?: ')
    run_times.append(name)
    age = int(input('What is your age?: '))
    run_times.append(age)
    run_time = input('What was your completed running time in minutes?: ')
    run_times.append(run_time)
#-----main-----------------------
if(__name__== "__main__"):
    main()