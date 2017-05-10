def main():
    infile = open('fees.txt', 'r')
    fees = infile.readlines()
    infile.close()

    print('The list "Fees" after reading from the file.')
    print(fees)
    print(' ')
    print('========================================================')
    print(' ')

    i = 0
    while i < len(fees):
        fees[i] = fees[i].rstrip('\n')
        i += 1

    print('The list "Fees" after removing the endline.')
    print(fees)
    print(' ')
    print('========================================================')
    print(' ')
    headings = ['Airline', '1st Bag', '2nd Bag', 'Change Fee', 'Other Fee', 'Feels Like']
    southwest = fees[0:6]
    jetBlue = fees[6:12]
    alaska = fees[12:18]
    delta = fees[18:24]
    united = fees[24:30]
    american = fees[30:36]
    spirit = fees[36:42]

    # print(southwest)
    # print(jetBlue)
    # print(alaska)
    # print(delta)
    # print(united)
    # print(american)
    # print(spirit)

    print('Now the final table.')
    print(' ')
    print('\t\t'.join(headings))
    print('\t\t'.join(southwest))
    print('\t\t'.join(jetBlue))
    print('\t\t'.join(alaska))
    print('\t\t'.join(delta))
    print('\t\t'.join(united))
    print('\t\t'.join(american))
    print('\t\t'.join(spirit))


main()
