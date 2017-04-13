#In this test you will complete an incomplete program. You will write a program to input three numbers from the user, find the largest of the three numbers, and display the three numbers along with the largest numbers. You cannot change any of the existing code provided - you can just add to it.

def main():
	# Please see the comments
    largest = 0
    #insert call to function get_input() after the = sign on the following three lines
    number1 = get_input()
    number2 = get_input()
    number3 = get_input()
    print(' ')
    #print(number1)
    #print(number2)
    #print(number3)
	
    # insert call to function find_largest after this comment.
	# find_largest will take in three parameters and will return the largest of the 3 numbers
    largestNum = find_largest(number1, number2, number3)
    #print(largestNum)
    
    #Insert the statement to display the three numbers entered and the largest number after this comment.
    #The print statements will be in a function named display_results()
    display_results(number1, number2, number3, largestNum)

	
	
#Add the code for three functions:

#Add the function calls as listed in the attached file
#find_largest( ):Enter the parameters for the function find_largest( ). The parameters will be the three numbers that were part of the input process in main( ). These numbers will be passed to find_largest. Write the code for find_largest( ) to find the largest of the three numbers.
def find_largest(num1, num2, num3):
	# insert parameters in the parenthesis
	# Write the code for this function here.
	# find_largest will take in three parameters and will return the largest of the 3 numbers
	# These three numbers are passed in as parameters from the main function
	# Hint: if and elif - no loop needed here
	if num1 > num2 and num1 > num3:
		return num1
	elif num2 > num1 and num2 > num3:
		return num2
	else:
		return num3

#get_input( ): This function will input a number and return it. The function will be called three times in main( ) to input three numbers.
def get_input():
    #insert a statement to input a number
    inputResults = int(input('Please type in a whole number for this program! '))
    #return this number out of this function
    return inputResults

#display_results( ): This function will display the three numbers entered and will display the largest of the three. All four numbers will need to be passed in as parameters. Use appropriate labels and spacing for the output.
def display_results(num1, num2, num3, num4):
    #this function will display the three numbers and the largest of the three
    #the three numbers and the largest number will be passed into this function as parameters
    print('First number: ', num1)
    print('Second number: ', num2)
    print('Third number: ', num3)
    print('  ')
    print('The largest of the three numbers you input is: ', num4) 

main()
# this is the call to main() that will make the program run
