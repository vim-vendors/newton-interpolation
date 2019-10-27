import numpy
import pdb

def Coef(n, x_array, y_array, a_array):
	for x in range(0, n):
		a_array[x] = y_array[x]
	for j in range(1, n):
		for i in range(n-1, j-1, -1):
			a_array[i] = (a_array[i] - a_array[i - 1]) / (x_array[i] - x_array[i - j])
			# pdb.set_trace()
#end Coef

def Eval(n, x_array, a_array, t):
	temp = a_array[n - 1]
	for i in range(n-2, -1, -1):
		temp = temp * (t - x_array[i]) + a_array[i] 
	return temp
#end Eval

testn = 5
testx = [3.0, 1.0, 0.0, 4.0, 7.0]
testy = [1.0, 0.12, -0.3, 2.0, 2.5]
testa = [0.0, 0.0, 0.0, 0.0, 0.0]

# print("Coef Print")
# print(testn)
# print(testx)
# print(testy)
# print(testa)
# Coef(testn, testx, testy, testa)
# print("Coef Post")
# print(testn)
# print(testx)
# print(testy)
# print(testa)

# print("Eval Print")
# print(testn)
# print(testx)
# print(testy)
# print(testa)
# print("Eval value is ",  end=" ")
# print(Eval(testn, testx, testa, 2))
# print("Eval Post")
# print(testn)
# print(testx)
# print(testy)
# print(testa)