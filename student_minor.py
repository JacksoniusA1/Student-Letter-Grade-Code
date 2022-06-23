#print the menu
print("Select option from Menu /n------------------")
print("1. Login")
print("2. Create User")

#prompt and get the option the user selected
while True: 
    user_option=input("would you like to (1) login or (2) creat account? ")

    #Ensure the user entered a valid option (1 or 2)
    if user_option != "1" and user_option != "2":
        print("ERROR: Enter a 1 or 2")
        continue
    else: 
        print("Yaya! Good input")
        break
    # -if not, prompt user again

#if the user chose 1, ask for user name and password
# -check username and password combination in the users.txt file
# - if not a valid combination re-prompt the user. 
# - if valid then move on to prompt for student data

#If the user chose 2, ask for username and password
# - valiate username and password length. If valid, write to users.txt file
#- and move on
#If not valid re prompt user

#Ask user how many students to enter data for
#prompt uer to enter student name and number score
#store data somewhere
#convert the number grade score to a letter grade

#print student data(name, score, grade)
#calculate school class average



