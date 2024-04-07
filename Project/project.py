

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
	country = input("Entry Country: ")
	cursor = db.cursor()
	sql = "select ci.name, ci.district, ci.population, co.name as country_name from city ci inner join country co on ci.countrycode = co.code where co.name like %s"

	values = ("%"+country+"%",)
	cursor.execute(sql, values)
	result = cursor.fetchall()
	lines = 0
	for x in result:
		print(x)
		lines = lines+1
		if lines == 2:
			next = input("Press any key to continue or q to quit: ")
			lines = 0
			if next == "q":
				break
	#if choice != "q": # Probably should be a while loop when doing the real thing
		
def update_population():
	result=""
	city_id = int(input("Enter City ID: "))
	cursor = db.cursor()
	sql = "select ci.name, ci.district, ci.population from city ci where ci.id = %s"
	values = (city_id,)
	cursor.execute(sql, values)
	result = cursor.fetchall()
	if len(result) == 1:
		print(result)
		to_do = ""
		while to_do not in ("D", "d", "I", "i"):
			to_do = input("[I]ncrease/[D]ecrease Population: ")
			if to_do in "I, i":
				symbol = "+"
				#https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/
				sql = "update city set population = population + %s where ID = %s"
			elif to_do in "D, d":
				symbol = "-"
				sql = "update city set population = population - %s where ID = %s"
			else: 
				print("Try Again...")
				to_do=""
		how_much = int(input("Enter Population "))
		values = (how_much,city_id,)

		cursor.execute(sql, values)
		db.commit()
	else:
		print ("try Again...")


	

	
	#for x in result:
#		print(x)
#	time.sleep(3)


def add_person():
	print("Adding Person")
	id = int(input("ID: "))
	name = input("Name: ")
	age = int(input("Age: "))
	salary = input("Salary: ")
	city_id = int(input("City ID: "))

	# Checks for personid and city
	cursor = db.cursor()
	sql = "select * from person where personid = %s"
	values = (id,)
	cursor.execute(sql, values)
	result = cursor.fetchall()

	cursor2 = db.cursor()
	sql = "select * from person where city = %s"
	values2 = (city_id,)
	cursor2.execute(sql, values2)
	result2 = cursor2.fetchall()

	if len(result) != 0:
		print("Person Id", id, "already exists")
		time.sleep(3)
		display_menu()
	elif len(result2) == 0:
		print("City ID", city_id, "does not exist")
		time.sleep(3)
		display_menu()
	else:
		cursor = db.cursor()
		sql = "insert into person values (%s, %s, %s, %s, %s)"
		values = (id, name, age, salary, city_id,)
		cursor.execute(sql, values)
		db.commit()
		print("Update Complete")
		time.sleep(3) # Replace with a "press c to continue or something"

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
	time.sleep(3) # Replace with a "press c to continue or something"


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
