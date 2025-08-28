'''
    author: Conner Larson-Snow
    date: 25/08/25
    version: 1
    description: This code is to collect data from the user and store the values in a list
'''
#--------libraries---------------
import random
#--------functions---------------
def parse_time_input(time_str):
    """Convert MM:SS or SS format to minutes as float."""
    if ':' in time_str:
        try:
            minutes, seconds = map(int, time_str.split(':'))
            return minutes + seconds / 60
        except ValueError:
            raise ValueError("Invalid format. Use MM:SS or SS.")
    else:
        try:
            return float(time_str) / 60  # assume input is in seconds
        except ValueError:
            raise ValueError("Invalid numeric input.")

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
        while True:
            time_input = input(f"Enter run time #{i+1} (MM:SS or seconds): ")
            try:
                run_time_minutes = parse_time_input(time_input)
                run_times_list.append(run_time_minutes)
                break
            except ValueError as e:
                print(e)


        average_run_time = sum(run_times_list) / len(run_times_list)

        print("\nSummary: ")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print("Run Times:", run_times_list)
        print(f"Average Run Time: {average_run_time:.2f}")

#-----main-----------------------
if(__name__== "__main__"):
    main()