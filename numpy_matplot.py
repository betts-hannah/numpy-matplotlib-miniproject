# Hannah Betts
# Scientific Computing
# Due 04/08/2024

import numpy as np
from numpy import random

row = int(input("Please Enter the number of Rows for your seating chart:  "))
column = int(input("Please Enter the number of Columns for your seating chart:"))


if __name__ == '__main__' : 
	chart = np.array([])
	students = ["Hannah", "Ethan", "Andrew", "Ben", "Jackson", "Ruthie", "Sarah", "Rachelle", "Daniel", "Makih", "Cole", "Carl", "Ian", "Katie", "Chloe", "Kennedy", "Mckenna", "Kylee", "Haily", "Bri", "Ty", "Dylan"]
	
	#Randomizing seating chart from the list of student names
	for i in range(row):
		for h in range(column):
			random_name = random.choice(students)
			#Random student name gets put into the array
			chart= np.append(chart, f"{random_name} ({i}, {h})")
			#This removes that Students name from list of students
			students.remove(random_name)
	#Now we have to reshape the array to be row  and columns
	chart = chart.reshape(row, column)

	#This will give us seating chart with the position of each student (row, column)
	for i in range(row):
		for h in range(column):
			if h  < column -1:
				print(chart[i,h], end=" ")
			else:
				print(chart[i,h], end="\n")

