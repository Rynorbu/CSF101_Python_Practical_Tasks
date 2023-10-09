#Task 26
#Define a variable called number1 and give it a value of “a”
#Define another variable called number2 and give it a value of “b”
#What is the type of the variable number1 and number2
#Compare if number1 is greater than number2 using “>” operator
#Store/assign the result of comparison into another variable called result
#Display the result variable as an output using the print() function

number1 = "a" #string type
number2 = "b" #string type

result = number1 > number2  
print(result)
 
# the output is false because we cannot compare two string with operation ">"




#Task 26
#Define a variable called variable1 and give it a value of True
#Define another variable called variable2 and give it a value of False
#Define another variable called variable3 and give it a value of False
#Define another variable called variable4 and give it a value of False
#Compare the variables using “or” operator:
#Store/assign the result of comparison into another variable called result
	#result = variable1 or variable2 or variable3 or variable4
#Display the result variable as an output using the print() function

variable1 = True
variable2 = False
variable3 = False
variable4 = False

result = variable1 or variable2 or variable3 or variable4
print(result)
# the output is True because variable1 is true, the "or" operator doesnot evalute the remaining variables.

#Task 26
#Define a variable called variable1 and give it a value of True
#Define another variable called variable2 and give it a value of False
#Define another variable called variable3 and give it a value of False
#Define another variable called variable4 and give it a value of False
#Compare the variables using “and” operator:
#Store/assign the result of comparison into another variable called result
	#result = variable1 and variable2 and variable3 and variable4
#Display the result variable as an output using the print() function


variable1 = True
variable2 = False
variable3 = False
variable4 = False

result = variable1 and variable2 and variable3 and variable4
print(result)

# the output is fasle because the and operator compare to all the variables, the variable2, variable3, variable4 is False. It will be true only if all the values in the variables are true
