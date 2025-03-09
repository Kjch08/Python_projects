print("Roadmap provider project.")

print("Are you a fresher or experienced?")
#get users choice for fresher or experienced

user_choice = input("Enter your choice: ").upper() # upper() will convert the user choice to upper case.

if user_choice == 'FRESHER':
    print("You selected fresher")
    print("These are the options for fresher: Web Dev, App Dev, DS ML AI")
    #based on choice it will explore more options in fresher and experienced
    selected = input("Enter your choice for fresher course: ").lower() # will return user input in lower case
    if selected == 'web dev':
        print("Under this course you will learn HTML, CSS, JS, PYTHON, DJANGO")
    elif selected == 'app dev':
        print("Under this course you will learn JAVA + DSA + Build projects")
    elif selected == 'ds ml ai':
        print('Learn Python, Maths, R')
    else:
        print("Invalid choice. Please select one of the options provided.")
 #for the experienced 
elif user_choice == 'EXPERIENCED':
    print("You selected experienced")
    print("These are the options for experienced: Data Analytics, Cloud Computing, Back End")
    selection = input("Enter your choice for th course for experienced: ").lower()
    if selection == 'data analytics':
        print("Learn Python, Excel, Power BI")
    elif selection == 'cloud computing':
        print("Learn DevOps and Python for automation")
    elif selection == 'back end':
        print("Learn Python and Django for backend")
    else:
        print("Invalid choice. Please select one of the options provided.") #if user enters option which is not available

else:
    print("Invalid choice: please choose either fresher or experienced")  #if user enters any thing which is not in option it will report this.
