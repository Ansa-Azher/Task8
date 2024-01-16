
    #*******pseudo code*********
    #This program will take input from the user and than find the cube of all numbers till the nuber user entered
    #The program will as user to enter a number that you dont want to find the cube
    #for loop is used to iterate the  from start to user input 
    #and than we used if to met the user requirment to not find the cube of specific number
    #each time program will find the cube of number it will display the cube of number along the number on screen 
    
    


# input function will take input from the user and int function will convert it into into for calculation
user_input= int(input("please enter a number to find the cube of all numbers till that number"))
No_cube = int(input("Please enter a number of which you dont want to find the cube"))

# cube variable is intilized by 1
cube = 1

# for loop is used to to iterate the number till user input to find cube of all number
# here we add 1 to user input in range so it will iterate exactly till the number what user entered
for i in range(1,user_input + 1):
    
    #   if condition wiil mtch the number with user number to not to find the cube
        if No_cube == i:
            # Here we make logical error, we should use 'continue' to skip the number
            # but here we use break that if loop reach the number that user dont want cube of that number
            # l=break statment will exit the loop body and will not perform function on rest of numbers
            break
        
        #cube variable is used to store the cube of each number
        cube = i ** i
        # print statement is used to print the cube of number along the number
        print(f"cube of {i} is {cube} ")              