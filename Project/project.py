

# Main function
def main():
	# Initialise array
#	array = []

	display_menu()
	
	while True:
		choice = input("Choice: ")
		
		if (choice == "1"):
			view_cities()
			display_menu()
		elif (choice == "2"):
			update_population()
			display_menu()
		elif (choice == "3"):
			add_person()
			display_menu()
		elif (choice == "4"):
			delete_person()
			display_menu()
		elif (choice == "5"):
			view_by_pop()
			display_menu()
		elif (choice == "6"):
			view_twinned()
			display_menu()
		elif (choice == "7"):
			twinned_with_dublin()
			display_menu()
		elif (choice == "8"):
			test_select()
			display_menu()
		elif (choice == "x"):
			break;
		else:
			display_menu()
			
def view_cities():
	print("Viewing Cities")
	choice = input("Entry Country: ")
	if choice != "q": # Probably should be a while loop when doing the real thing
		print("Showing the details")
		
def update_population():
	print("Updating Population")
	choice = input("Enter City ID: ")

def add_person():
	print("Adding Person")
	id = int(input("ID: "))
	name = input("Name: ")
	age = int(input("Age: "))
	salary = input("Salary: ")
	city_id = int(input("City: "))

def delete_person():
	print("Deleting Person")
	to_del = input("Enter ID of person to delete: ")

def view_by_pop():
	print("View Countries by Population")
	to_do = input("Enter < or > : ")
	value = input("Enter population : ")

def view_twinned():
	print("View Twionned Cities")
	print ("Twinned Cities")
	print ("--------------")

def twinned_with_dublin():
	print("Twinning with Dublin")
	city_to_twin = input("Enter ID of City to twin with Dublin : ")

def test_select():
	cursor = db.cursor()
	sql = "select * from student where id = %s"
	values = (3,)
	cursor.execute(sql, values)
	result = cursor.fetchall()
	for x in result:
		print(x)
	time.sleep(3)


'''
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
'''
'''
def find_gt_in_array(array):
	num=int(input("Enter Num: "))
# https://stackoverflow.com/questions/4587915/return-list-of-items-in-list-greater-than-some-value
	list = [x for x in array if x > num]
	print(list)
'''


def display_menu():
#	import os
	os.system('clear')
	print("=" * 60)
	print("                             MENU")
	print("=" * 60)
	print("1 - View Cities by Country")
	print("2 - Update City Population")
	print("3 - Add New Person")
	print("4 - Delete Person")
	print("5 - View Countries by population")
	print("6 - Show Twinned Cities")
	print("7 - Twin with Dublin")
	print("8 - Test Select")

	print("x - Exit application")

if __name__ == "__main__":
	import os
	import mysql.connector
	from config import config as cfg
	import mysql.connector
	import time

	db = mysql.connector.connect(
    host=cfg["host"],
    user = cfg["user"],
    password = cfg["password"],
    database = cfg["database"]
)
	# execute only if run as a script 
	main()
