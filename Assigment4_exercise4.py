import numpy
import pdb
import re
import sys
import time

def Coef(n, x_array, y_array, a_array):
	for x in range(n):	
		a_array[x] = y_array[x]	
	for j in range(1, n):
		for i in range(n-1, j-1, -1):
			a_array[i] = (a_array[i] - a_array[i - 1]) / (x_array[i] - x_array[i - j])
#end Coef

def Eval(n, x_array, a_array, t):
	temp = a_array[n - 1]
	for i in range(n-2, -1, -1):
		temp = temp * (t - x_array[i]) + a_array[i] 
	return temp
#end Eval

# exercise 4

#interface with user
print("Press Q/q to quit.")
value = input("Please provide a numerical value (i.e. 2) to be used to generate n number of random values : ")
try:
	if (value == 'q' or value == 'Q'):
		print("Exiting now......") 
		sys.exit()
	else:
		value = int(value) + 0
except ValueError:
	print("Wrong arguments passed. End program.")
	sys.exit()

#time the script, ends when method is called and completes
start_time = time.time()
#generate data based on n inputs
# random_x = []
stringX = ""
stringY = ""
# random_y = []
for x in range(value):
	rando = numpy.random.uniform(-10.0, 10.0)
	# random_x.append(rando)
	stringX += (str(rando) + " ") 
for y in range(value):
	rando = numpy.random.uniform(-10.0, 10.0)
	# random_y.append(rando)
	stringY += (str(rando) + " ") 

#write data to file
#write solutions/output to file
outputSol = "generated_values.txt"
outputFile = open(outputSol, 'w')
outputFile.write(stringX)
outputFile.write(stringY)
outputFile.close()

#extract file info and parse with regex
helloFile = open("generated_values.txt", 'r')
helloContent = helloFile.read()
p = re.compile('\n')
n = len(p.findall(helloContent)) - 1
p = re.compile('-?[0-9]+.[0-9]+')
string_array = p.findall(helloContent)
newtonList = []
for x in range(len(string_array)):
	newtonList.append(float(string_array[x]))

x_list = []
y_list = []
#number of data points
size = len(x_list)
coeff_list = []

for x in range(int(len(newtonList) / 2)):
	coeff_list.append(newtonList[x] * 0.0)
y = 0
for x in range(int(len(newtonList) / 2)):
	x_list.append(newtonList[x])
	y = x
for x in range(y + 1, len(newtonList)):
	y_list.append(newtonList[x])


#compute time taken to run

Coef(len(x_list), x_list, y_list, coeff_list)
#evaluate at random points ie x = ???
print("The evaluation value is ",  end=" ")
print(Eval(len(x_list), x_list, coeff_list, numpy.random.uniform(-10.0, 10.0)))
print("Time to run is ....")
print("--- %s seconds ---" % (time.time() - start_time))

helloFile .close()
