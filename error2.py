# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# put the inverted comma on the lion to make it string(run time error)
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

#write f in the start of line to make it 'f' string and swap the variable 'animal_type' with the 'number_of_teeth'(logical error)
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

# put the braces for print function(syntax errror)
print(full_spec)