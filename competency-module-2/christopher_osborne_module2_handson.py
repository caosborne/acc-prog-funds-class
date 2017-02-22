# Write a complete and correct Python program that does the following:

# The program will input:
#     The length and width of a rectangle
#     The side of a square
#     The radius of a circle
counter = 0
while counter < 3:
    rectangleLength = float(input('What is the length of the rectangle?'))
    rectangleWidth = float(input('What is the width of the rectangle?'))
    squareSide = float(input('What is the length of the side of a square?'))
    circleRadius = float(input('What is the radius of the circle?'))

    # The following input validations will be performed:
    #     The user cannot enter any value less than zero ( 0 )
    #     The user will only get three chances to enter a correct value. This must be done in a loop
    if rectangleLength < 0 or rectangleWidth < 0 or squareSide < 0 or circleRadius < 0:
        print('You cannot enter values of less than 0. Please try again!')
        print(' ')
        counter += 1
    else:
        # print('This is working correctly!')
        # The program will calculate:The program will now compare the three calculated areas to ascertain which is the largest area
        #     The area of the rectangle
        #     The area of the square
        #     The area of a circle
        rectangleArea = format(rectangleWidth * rectangleLength, '.2f')
        squareArea = format(squareSide ** 2, '.2f')
        circleArea = format((3.14159265359 * (circleRadius ** 2 )), '.2f')

        # print('The area fo the rectangle is: ', rectangleArea)
        # print('The area of the square is: ', squareArea)
        # print('The area of the circle is: ', circleArea)
        print('  ')
        print(format('Rectangle Area', '<20'),format('Square Area', '^20'), format('Circle Area', '>20'))
        print(format('--------------', '<20'),format('-----------', '^20'), format('-----------', '>20'))
        print(format(rectangleArea, '<20'),format(squareArea, '^20'), format(circleArea, '>20'))
        print('======================================================================')
        print(' ')
        # At the end the program will display the three areas to the user and also inform the user which shape has the largest area using a set of formatted print statements
        if rectangleArea > squareArea and rectangleArea > circleArea:
            print('The rectangle area of ', rectangleArea,' is the largest!',end='\n')
        elif squareArea > rectangleArea and squareArea > circleArea:
            print('The square area of ', squareArea,' is the largest!',end='\n')
        else:
            print('The circle area of ', circleArea,' is the largest!',end='\n')
        break

else:
    print('Sorry you have entered an incorrect value for one of the sides on multiple occasions. The program has ended due to 3 failed attempts.')
