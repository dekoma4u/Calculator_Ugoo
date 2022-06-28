from calc_func import division, add, multiplication, subtract #functions imported

#While loop is used
while True:
    
#While loop is used here to verify input
    while True:
        print("Type only numbers and characters")
        first_num = float(input("Type your first number here:\n"))
        try:
            val = int(first_num)
            break
        except ValueError:
            print(f" {first_num} is not a number")

#Made a list of math operator and check for content of the list    
    operator_check = ["*", "+", "-", "/"]
    operator_sign = input("Type math operator, eg. 'x' for multiply or '+' for add:\n") 
    if operator_sign in operator_check:
        
#When condition was passed, it allowed the second input and checked for validity of the input        
        while True:
            second_num = float(input("Type your second number here:\n"))
            try:
                val = int(second_num)
                float(second_num)
                break
            except ValueError:
                print(f" {second_num} is not a number")
#The math functions were called from another module with the right parameters
        if operator_sign == "+":
            add(first_num, second_num)
        elif operator_sign== "-":
            subtract(first_num, second_num)
        elif operator_sign== "*":
            multiplication(first_num, second_num)
        elif operator_sign== "/":
            division(first_num, second_num) 
        else:
            print(f" Your input {operator_sign} is not a valid operator")
    else:
        print(f" {operator_sign} is not a math operator:\n")

#Made condition of continuing if an error was encountered
        exit1 = input("Click 'y' or 'n' to either continue or stop:\n") 
        if exit1 == "y":
            continue
        elif exit1 == "n":
            print("Thank you for using Ugoo calculator. Hope to see you soon:\n")
            break
        else:
            print("I can not recognize your input, start afresh")
            break  
         
#The initial while loop was terminated here     
    break
