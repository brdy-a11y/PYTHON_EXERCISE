''' 1) Write a program to demonstrate different numeric data types
 (int, float) and type conversion. '''

x = 5 
print(f"x : {x} | type : {type(x)}")  # integer datatype
y = 6.66  
print(f"y : {y} | type : {type(y)}") # float datatype

print(f'x : {x} | typecasting into float => x : {int(x)}')  # type conversion from integer to float type.

print(f'y : {y} | typecasting into integer => y : {int(y)}')  # type conversion from float to integer type.

# ----------------------------------------------------------

# converting string to integer :
age = input("Enter age : ")
age_int = int(age)
print(f"before conversion => age : {age} | type : {type(age)} ")
print(f"age : {age_int} | type : {type(age_int)}")