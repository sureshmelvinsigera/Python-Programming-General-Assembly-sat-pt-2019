first_name = "Thomas"
middle_name = "Mapother"
last_name = "Cruise"

print("First name is ", type(first_name))
print("Middle name is ", type(middle_name))
print("Last name is ", type(last_name))
print("Converting to upper-case ", first_name.upper())
print("Converting to lower-case", first_name.lower())
print("Length of the first name is ", len(first_name))
print("Length of the middle name is ", len(middle_name))
print("Length of the last_name is ", len(last_name))

first_name = first_name.replace("Thomas", "Tom")

print(first_name, middle_name, last_name)
