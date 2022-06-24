#print the menu
print("Select option from Menu /n------------------")
print("1. Login")
print("2. Create User")

#prompt and get the option the user selected
while True: 
    user_option=input("would you like to (1) login or (2) creat account? ")

    #Ensure the user entered a valid option (1 or 2)
    if user_option != "1" and user_option != "2":
        # -if not, prompt user again
        print("ERROR: Enter a 1 or 2")
        continue
    else: 
        print("Yay! Good input")
        break



if user_option == "1": 
    while True:
        #if the user chose 1, ask for user name and password
        user_name= input("please enter your user name: ")
        user_pass= input("please enter your password: ")
        # -check username and password combination in the users.txt file
        #open the users files
        user_file = open("users.txt", "r")
        user_found= False
        for line in user_file:
            credentials = line.split(", ")
            if user_name == credentials[0] and user_pass == credentials[1].rstrip():
                user_found = True
                break

        if user_found:
                print(f"User {user_name} successfully logged in!")
                break
        else:
            print(f"{user_name} not found! \n")
        #read the lines from the file
        #compare username and password for a match      
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
