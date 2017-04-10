def main():
    # Create a simple text file in which you will store the numbers 0 through 10, each on a separate line.
    # Now write a program that does the following:
    numbers = []
    i = 0
    while i < 11:
        # Strip the list of the end of line markers or the "\n"
        numbers.append(i)
        i += 1
    print(numbers)
    # outfile = open('christopherOsborneNumbers.txt', 'w')
    for num in numbers:

    n = 0
    while n < len(numbers):
        numbers = str(numbers[n]) + '\n'
        print(numbers)
    # outfile.close()
    print(numbers)

main()

# This was written first and I struggled with it so I tried the easier one which is ^^^^. 

# def main():
#     try:
#         # Open numbers.txt in append mode
#         infile = open('numbers.txt', 'r')
#         # Read the numbers into a list
#         numbers = infile.readlines()
#         infile.close()
#         # print(numbers)
#         i = 0
#         while i < len(numbers):
#             # Strip the list of the end of line markers or the "\n"
#             numbers[i] = int(numbers[i].rstrip('\n'))
#             i += 1
#             num = 0
#             while num < 21:
#                 if num == numbers:
#                     num += 1
#                     print("this is working")
#                 else:
#                     numbers = numbers[i] + 1
#                     print(numbers)
#                     num += 1
#         print(' ')
#         # print(numbers)
#         # Append the numbers 11 through 20 to this list (done in a loop)
#         # for count in range(1, 21):
#         #     if numbers == numbers:
#         #         count += 1
#         #     else:
#         #         numbers += 1
#         # print(numbers)
#
#         # print(numbers)
#         # if num in numbers < 21:
#         #     numbers
#         # Write the list back to the numbers file - you will insert a tab "\t" after each number
#         # You will use a loop to read from and write to the file
#         # Write an exception that will be raised if the program is unable to open the files.
#
#
#
#     except IOError:
#         print('An error occurred trying to read the input file. Please try again!')
#
# main()
