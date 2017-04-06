def main():
    length = 'length'
    radius = 'radius'
    squareStr = 'square'
    circleStr = 'circle'
    # Asks the user for a length and a width of a rectangle. This input will happen in a function and will then be returned from a function.
    recLengthInput = recLength()
    recWidthInput = recWidth()

    # Asks the user for the side of a square.  This input will happen in a function and will then be returned from a function.
    squareLength = squareCircle(length, squareStr)

    #  Asks the user for a radius of a circle. This input will happen in a function and be returned from a function. You will reuse the same function as the square.
    circleRadius = squareCircle(radius, circleStr)

    # Uses a function to calculate and print the areas of all three.
        # The area of a rectangle is length times width
        # The area of a square is side times side
        # The area of a circle is pi times r  squared
    areaOfAll = area(recLengthInput, recWidthInput, squareLength, circleRadius)

def recLength():
    rectangleLength = float(input('What is the length of the rectangle? '))
    return rectangleLength

def recWidth():
    rectangleWidth = float(input('What is the width of the rectangle? '))
    return rectangleWidth

def squareCircle(str1, str2):
    radiusSideLength = float(input('What is the ' + str1 + ' of the ' + str2 + '? '))
    return radiusSideLength

def area(num1, num2, num3, num4):
    rectangleAreaCalc = num1 * num2
    print('Rectangle Area: ', rectangleAreaCalc)

    squareArea = num3 ** 2
    print('Square Area: ', squareArea)

    circleArea = (3.14159265359 * (num4 ** 2 ))
    print('Circle Area: ', circleArea)


main()
