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
#Convert MM:SS or SS format to minutes as float
    if ':' in time_str:
        try:
            minutes, seconds = map(int, time_str.split(':')) #splits the string into minutes and seconds
            return minutes + seconds / 60 #converts total time to minutes
        except ValueError:
            raise ValueError("Invalid format. Use MM:SS or SS.") #raise error if input is not properly formatted

    else:
        try:
            return float(time_str) / 60  #convert seconds to minutes
        except ValueError:
            raise ValueError("Invalid numeric input.")  #raise error if input is not a valid number

def main():
    name = ''
    age = ''
    run_times_list = [] #list to store run times in minutes
    run_times_inputs = 5 #number of run times to collect

    name = input('What is your name?: ')

    #loop until a valid age of 14 or older is entered
    while True:
        try:
            age = int(input('How old are you?: '))
            if age >= 14:
                break #exit loop if age is valid
            else:
                print("Your age is invalid. You must be 14 or older.")
        except ValueError:
                print("Please input a valid number for your age.")

    #collect run time inputs from the user
    for i in range(run_times_inputs):
        while True:
            #prompt user for run time in MM:SS or seconds format
            time_input = input(f"Enter run time #{i+1} (MM:SS or seconds): ")
            try:
                #convert input to minutes and add to list
                run_time_minutes = parse_time_input(time_input)
                run_times_list.append(run_time_minutes)
                break #exit inner loop if input is valid
            except ValueError as e:
                #display error message and retry
                print(e)

        #calculate average run time after each entry
        average_run_time = sum(run_times_list) / len(run_times_list)

        #display summary after each entry
        print("\nSummary: ")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print("Run Times:", run_times_list)
        print(f"Average Run Time: {average_run_time:.2f}")

#-----main-----------------------
#entry point of the program
if(__name__== "__main__"):
    main()