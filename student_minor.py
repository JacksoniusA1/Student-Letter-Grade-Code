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
elif user_option == "2":
    while True:
        user_name= input("please enter your user name: (4-12 characters)")
        user_pass= input("please enter your password: (6-16 characters)")


    #get username and password length
        user_name_length= len(user_name)
        password_length= len(user_pass)
        print(user_name_length)
        print(password_length)

    # - valiate username and password length. If valid, write to users.txt file
        if (user_name_length>=4 and user_name_length<=12) and ( password_length>= 6 and password_length<= 16):
            print("yay good username and password!")
            #write username and password to the file
            user_file= open("users.txt" , "a")
            user_file.write(f"{user_name}, {user_pass}\n")
            user_file.close()
            break
        else:
            print("Error! Incorrect username or password length.\n")
#- and move on
#If not valid re prompt user
print("Ask user for student data")  
#Create 3 empty lists for student name, scores, letter grades
student_names_list = []
student_scores= []
student_letter_grades= []
#Ask user how many students to enter data for
number_of_students= int(input("Enter the number of students to enter grades for: "))
for counter in range(number_of_students):
    
        
    #prompt user to enter student name and number score
    student_names= input("Enter student name: ")
    student_score= float(input("Enter student score: "))
    #store data in the lists
    student_names_list.append(student_names)
    student_scores.append(student_scores)
    #convert the number grade score to a letter grade
    if student_score >=90:
        student_letter_grades.append("A")
    elif student_score >=80:
        student_letter_grades.append("B")
    elif student_score >=70:
        student_letter_grades.append("C")
    elif student_score >=60:
        student_letter_grades.append("D")
    else:
        student_letter_grades.append("F")
#print student data(name, score, grade)
for index in range (len(student_names)):
    print(f"{student_names[index]} : {student_scores[index]} : {student_letter_grades [index]}")
    #calculate school class average
    #school_class_average = (student_score[index])/number_of_students
#print(f"school class average: {school_class_average}")
total=0
#for score in student_scores:
    #total = score + total
average= sum(student_scores)/ len(student_scores)
#for index in range(len(student_scores)):
  #  total= total + student_scores[index]
    #average=total/len(student_scores)
print("your average is:{average}")
