# Write an if-else statement that prints 'Average price' if the price is between 0 and 20. If it is greater than 20, the statement prints 'Outrageous price!'
#
# if price >= 0 and price <= 20:
#     print('Average price')
# else:
#     print('Outrageous price!')

# speed = 168
# if speed in range(0, 200):
#     print('The number is valid')

# s1 = ' New York'
# s2 = ' Boston'
#
# if s1 > s2:
#     print( s2 )
#     print( s1)
# else:
#     print( s1)
#     print( s2 )

num1 = int(input('Please enter the first number: '))

num2 = int(input('Please enter the second number: '))

num3 = int(input('Please enter the third number: '))

if num1 < num2 and num1 < num3:
    print(num1,' is largest',end='\n')
elif num2 < num1 and num2 < num3:
    print(num2,' is largest',end='\n')
else:
    print(num3, ' is largest', end='\n')
