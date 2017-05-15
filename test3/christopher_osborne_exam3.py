def main():
	#Open the file Exam3_file.txt in Read mode
	#Read the numbers in the file into a list
	infile = open('Exam3_file.txt', 'r')
	exam3 = infile.readlines()
	infile.close()
	i = 0
	while i < len(exam3):
		exam3[i] = exam3[i].rstrip('\n')
		i += 1
	#Create a new file in Append mode. The file must have your name as part of the file name.
	outfile = open('Exam3ChristopherOsborne.txt', 'a')
	#To this file:
		#Write your name and the date
		#Write the list you created in step 2
	name = 'Christopher Osborne'
	date = 'May 13, 2017'
	outfile.write(name + '\n' + date + '\n')
	item = 0
	for item in exam3:
		outfile.write(item + '\n')
	#Close the file
	outfile.close()
main()
