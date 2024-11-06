# Module 4: Activities: Lists and Tuples

# prompt the user for input of comma-separated values
user_input = input("Enter values of your choice separated by commas: ")
print("User input: \n", user_input)

# remove the commas and print values as lists
values_list = user_input.split(",")
print("List: \n", values_list)

# convert list into a tuple and remove commas
values_tuple = tuple(values_list)
print("Tuple: \n", values_tuple)



#Exercise 2

# [start the dictionary]

party = {
    
'money': 1000,
'cake': ['cheesecale', 'sponge cake', 'flourless cake', 'biscuit cake'],
'guests': ['Bob', 'Alicia', 'Eve', 'Tom', 'Harry'], 
'venue': ['outdoor', 'indoor', ]
}
#closes the dictionary

# Add a new key 'gifts' with a list of gift items
party['gifts'] = ['phone', 'laptop', 'camera', 'DIY card', 'chocolates']

#Add $500 to the existing value under the 'money' key
party['money'] =  party['money'] + 500  #added 500 using operator (+)

# Remove 'Bob' from the list under the 'guests' key
party['guests'].remove('Bob')

# Print the updated dictionary to see all changes
print("Updated Party Dictionary:", party)