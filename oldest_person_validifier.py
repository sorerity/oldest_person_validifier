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