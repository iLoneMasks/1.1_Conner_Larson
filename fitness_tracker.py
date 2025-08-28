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

    while True:
        try:
            age = int(input('How old are you?: '))
            if age >= 14:
                break
            else:
                print("Your age is invalid. You must be 14 or older.")
        except ValueError:
                print("Please input a valid number for your age.")


    for i in range(run_times_inputs):
        try:
            run_times = float(input(f"Please enter your run time #{i+1}: "))
            run_times_list.append(run_times)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        average_run_time = sum(run_times_list) / len(run_times_list)

        print("\nSummary: ")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print("Run Times:", run_times_list)
        print(f"Average Run Time: {average_run_time:.2f}")

#-----main-----------------------
if(__name__== "__main__"):
    main()