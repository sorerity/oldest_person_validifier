list = []

while True:
    while True:
        try:
            name = input("Please input your name: ")
        
            if not name.isalpha():
                print("Error, Name should not contain numbers.")
                continue

            age = int(input("Please input your age: "))

            if age <= 0 or age >= 110: 
                print("Error, Please input proper age.")
                continue

            oldest_person_validifier = {
                "Name": name,
                "Age" : age,
            }

            list.append(oldest_person_validifier)

            print(f"Name: {oldest_person_validifier['Name']}")
            print(f"Age: {oldest_person_validifier['Age']}")

            retry = input("Do you want to input another entry? Y/N:  ")
            break
        except:
            print("Error, age should not contain letters.")
            
    if retry == "N":
        if list:
            oldest_person = list[0]

            for person in list:
                if person["Age"] > oldest_person["Age"]:
                    oldest_person = person

            print(f"The oldest person is {oldest_person['Name']} with the age of {oldest_person['Age']}.")
        else:
            print("No valid entries were made.")
        break

    elif retry != "Y":
        print("Invalid input, stopping the program.")
        break




































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