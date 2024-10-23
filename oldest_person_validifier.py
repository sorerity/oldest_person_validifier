oldest_person_validifier = {}

while True:
    while True:
        try:
            name = input("Please input your name: ")
            age = int(input("Please input your age: "))
            if age >= 110: 
                print("Error.")
                continue

            oldest_person_validifier[name] = {
                "Name": name,
                "Age" : age,
            }

            print(oldest_person_validifier[name]["Age"])

            retry = input("Retry? Y/N:  ")
            break
        except:
            print("Error.")
            
    if retry == "N":
            break
    elif retry != "Y":
        print("Invalid")






































# Create a program that ask user to input name and age. Print error message when the input is not valid. Set your own definition of valid name and valid age. 
 #Store all the collected information into array. After every input, ask the user if want to input another entry. 
 #hen “Yes”, ask the user again for input. Do it until the user respond “No”. When the user responded “No”, display the name and age of the oldest person.
 #Use the array in checking who is the oldest.

#set main variable name 
#loop 1: 
#ask user to input name
#    if integer, print error
#ask user to input age
#    if letters, print error
#    if greater than 110, print error
#    if successful, put user inputs into an array
#        ask user if they want to input another entry
#            if yes, return loop 1
# if no, print name and age of the oldest person