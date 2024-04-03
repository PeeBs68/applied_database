
# Main function
def main():
	# Initialise array
	array = []

	display_menu()
	
	while True:
		choice = input("Enter choice: ")
		
		if (choice == "1"):
			array = fill_array()
			display_menu()
		elif (choice == "2"):
			print(array)
			display_menu()
		elif (choice == "3"):
			find_gt_in_array(array)
			display_menu()
		elif (choice == "4"):
			break;
		else:
			display_menu()
			
			
def fill_array():
	temparray=[]
	num=int(input("Enter Num: "))
	if num != -1:
		temparray.append(num)
	while num != -1:
		num=int(input("Enter Num: "))
		if num != -1:
			temparray.append(num)
	return temparray


def find_gt_in_array(array):
	num=int(input("Enter Num: "))
# https://stackoverflow.com/questions/4587915/return-list-of-items-in-list-greater-than-some-value
	list = [x for x in array if x > num]
	print(list)



def display_menu():
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - Fill Array")
    print("2 - Print Array")
    print("3 - Find > in Array")
    print("4 - Exit")

if __name__ == "__main__":
	# execute only if run as a script 
	main()
