# Name: Roan Campbell
# Date: 06/18/2023
# Description: Determine if a student will qualify for the Dean's List or Honor Roll via if else and while statements.
lastName = input("Please enter student's last name: ")
while lastName != "ZZZ":
    firstName = input("Please enter student's first name: ")
    GPA = float(input("Enter the student's GPA: "))
    if GPA >= 3.5:
        print("Congratulations -- {} {} has made the Dean's List.".format(firstName, lastName))
    else:
        if GPA >= 3.25:
            print("Congratulations -- {} {} has made the Honor Roll.".format(firstName, lastName)) 
    lastName = input("\nEnter Student Last Name: ")
   