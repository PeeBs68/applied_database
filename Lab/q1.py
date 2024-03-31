def main():
	# Initialise array
	array1 = [1,2,3,4,5,6,7,8,9,10]
	array2 = []
	for num in array1:
		array2.append(doubler(num))
#	print(array1)
	print(array2)

def doubler(num):
	num = num*num
#   print(num)
	return num

if __name__ == "__main__":
	# execute only if run as a script 
	main()