# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


# Done the correct indentation of program (syntax error or run time error)
# put the braces around the print function(syntax error)
print("Welcome to the error program")
# put the braces around the print function(syntax error)
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
 # remove one '=' symbol , == used for comparison not assigning(syntax error)
age_Str = "24" 
age = int(age_Str) 

# write f in start of linr in the print function to execute it and remove unwanted "+" and """" (run time error)
print(f"I'm  {age} years old.")

# Variables declaring additional years and printing the total years of age
#  remove "" around the variable value to make it integer , as we cant add string and integers(run time error)
years_from_now = 3
total_years = age + years_from_now

# put the braces for print function(syntax error)
# write the variable name ' total_years' instead of 'answer_years'(logical error)
print("The total number of years:", total_years)

# Variable to calculate the total amount of months from the total amount of years and printing the result
# correct the variable name from 'total' to 'total_years' (run time error)
# add the 6 in arithmatic expression for required output , as it says  on line 36 in print statement about 6 month as weel that no where added(logical error)
total_months = (total_years * 12) + 6

# put the braces for print function(syntax error)
# write f in start of linr in the print function to execute it and remove unwanted "+" and """" (run time error)
print(f"In 3 years and 6 months, I'll be {total_months} months old")

