



#Make a class calculator with the functions
class Calculator:
    #Title function
    def title(self):
        print("Calculator")
    #Message function
    def message(self):
        print("Please enter two numbers and operation")

    
    def menu_calculator():
        print("Please choose an option from the menu.")
        print("[1] Operation 1:","Addition")
        print("[2] Operation 2:","Subtraction")
        print("[3] Operation 3:","Multiplication")
        print("[4] Operation 4:","Division")
    menu_calculator()
        
    option = int(input("\nEnter your option: "))

    #perform calculations

    #While True to rerun the program if the user wish to
    while True:
        while option > 4:
            print("Invalid option. Please try again!") 
            option = int(input("\nEnter your option: "))
        if option == 1:
            print("Addition")
            try:
                #Get two numbers from the user
                add_num_1 = float(input("Please enter first number: "))
                add_num_2 = float(input("Please enter second number: "))
                #Perform the operation 
                sum_numbers = add_num_1 + add_num_2
                
                #Display the result
                print("The sum of two numbers is: ",sum_numbers, "\n")
            except ValueError:
                print("Do not put letters. Input numbers. Try again!")

        #if choice is subtraction
        elif option == 2:
            print("Subtraction")
            try:
                #Get two numbers from the user
                sub_num_1 = float(input("Please enter first number: "))
                sub_num_2 = float(input("Please enter second number: "))
                #Perform the operation 
                difference_numbers = sub_num_1 - sub_num_2
                
                #Display the result
                print("The difference of two numbers is: ",difference_numbers, "\n")
            except ValueError:
                print("Do not put letters. Input numbers. Try again!")
        
        #if choice is multiplication
        elif option == 3:
            print("Multiplication")
            try:
                #Get two numbers from the user
                mult_num_1 = float(input("Please enter first number: "))
                mult_num_2 = float(input("Please enter second number: "))
                #Perform the operation 
                product_numbers = mult_num_1 * mult_num_2
                
                #Display the result
                print("The product of two numbers is: ",product_numbers, "\n")
            except ValueError:
                print("Do not put letters. Input numbers. Try again!")
        
        #if choice is multiplication
        elif option == 4:
            print("Division")
            try:
                #Get two numbers from the user
                div_num_1 = float(input("Please enter first number: "))
                div_num_2 = float(input("Please enter second number: "))
                #Perform the operation 
                quotient_numbers = div_num_1 / div_num_2
                
                #Display the result
                print("The quotient of two numbers is: ", quotient_numbers, "\n")
            except ValueError:
                print("Do not put letters. Input numbers. Try again!")
            except ZeroDivisionError:
                print("You cannot put 0 on the second number")
                
        moredata = (input("Do you want to use the program again? \n[Yes] if continue \n[No] if exit \nEnter option: "))

        if moredata == "Yes" or "yes" or "Y" or "y" or "YES":
            menu_calculator()
            option = int(input("\nEnter your option: "))
            continue

        else:
            print("Thank you for using our program!")
            break

  


  