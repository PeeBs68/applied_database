

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
	print("Name\tDistrict\tPopulation\tName")
	#Note to self - maybe convert result to a list to format the output nicer
	#resultstr = [str(x) for x in result]
	#print (resultstr)
	for x in result:
		print(*x, sep ='\t')
		lines = lines+1
		if lines == 2:
			print("-- Quit (q) --")
			next = click.getchar()   # Gets a single character
			lines = 0
			if next == "q":
				break
			else:
				continue	
		
def update_population():
	result=""
	city_id = int(input("Enter City ID: "))
	cursor = db.cursor()
	sql = "select id, name, countrycode, district, population, latitude, longitude from city where id = %s"
	values = (city_id,)
	cursor.execute(sql, values)
	result = cursor.fetchall()

	while len(result) == 0:
		print("\nNo city found for ID = ", city_id)
		city_id = int(input("\nEnter City ID: "))
		cursor = db.cursor()
		sql = "select id, name, countrycode, district, population, latitude, longitude from city where id = %s"
		values = (city_id,)
		cursor.execute(sql, values)
		result = cursor.fetchall()

	if len(result) == 1:
		heads = ("ID", "Name", "CountryCode", "District", "Population", "Longitude", "Latitude")
		print(tabulate(result, headers = heads))
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

		#Probably overkill to do this bit but looks nice to me...
		cursor = db.cursor()
		sql = "select population from city where id = %s"
		values = (city_id,)
		cursor.execute(sql, values)
		result = cursor.fetchall()
		# https://stackoverflow.com/questions/33161448/getting-only-element-from-a-single-element-list-in-python
		[new]= result
		print(f"\nPopulation updated to {new[0]}, returning to main menu")
		#[new]= result
		#print(new[0])
		#for x in result:
		#	print(*x)
		time.sleep(3)
	else:
		print ("try Again...")


	

	
	#for x in result:
#		print(x)
#	time.sleep(3)


def add_person():
	print("Adding Person")
	id = int(input("ID: "))
	name = input("Name: ")
	age = input("Age: ")
	salary = input("Salary: ")
	city_id = input("City ID: ")

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
		while True:
			try:
				cursor = db.cursor()
				sql = "insert into person values (%s, %s, %s, %s, %s)"
				values = (id, name, age, salary, city_id,)
				cursor.execute(sql, values)
				db.commit()
				print("Insert Complete")
				time.sleep(3) # Replace with a "press c to continue or something"
				break
			except mysql.connector.Error as err:
        		# https://stackoverflow.com/questions/68438901/how-do-i-handle-mysql-exceptions-in-python
				print (f"Error: {err}")
				print("Returning to main menu")
				time.sleep(3)
				break
			

def delete_person():
	while True:
		try:
			print("Deleting Person")
			id = input("Enter ID of person to delete: ")
			cursor = db.cursor()
			sql = "select * from hasvisitedcity where personid = %s"
			values = (id,)
			cursor.execute(sql, values)
			result = cursor.fetchall()
			if len(result) != 0:
				print(f"Error: Can't delete Person ID: {id}. He/She has visited cities.")
				time.sleep(3)
				display_menu()
			else:
				cursor = db.cursor()
				sql = "delete from person where personID = %s"
				values = (id,)
				cursor.execute(sql, values)
				# https://stackoverflow.com/questions/2511679/python-number-of-rows-affected-by-cursor-executeselect
				rows_affected=cursor.rowcount
				#print(rows_affected)
				db.commit()
				if rows_affected == 0:
					print(f"No rows deleted - person_id {id} does not exist")
					time.sleep(3)
					break
				else:
					print(f"Person ID: {id} deleted - returning to main menu")
					time.sleep(3) # Replace with a "press c (using 'get' maybe)to continue or something"
					break
		except mysql.connector.Error as err:
			# https://stackoverflow.com/questions/68438901/how-do-i-handle-mysql-exceptions-in-python
			print (f"Error: {err}")
			time.sleep(3)
			break

def view_by_pop():
	print("View Countries by Population")
	to_do = ""
	cursor = db.cursor()
	while to_do not in (">", "<", "="):
		to_do = input("Enter < > or =: ")
		if to_do == ">":
			symbol = ">"
			sql = "select code, name, continent, population from country where population > %s"
		elif to_do == "<":
			symbol = "<"
			sql = "select code, name, continent, population from country where population < %s"
		elif to_do == "=":
			symbol = "="
			sql = "select code, name, continent, population from country where population = %s"
		else: 
			print("Try Again...")
			to_do=""
	pop = int(input("Enter Population "))
	values = (pop,)
	cursor.execute(sql, values)
	result = cursor.fetchall()
	heads = ("code", "name", "continent", "population")
	print(tabulate(result, headers = heads))
	#for x in result:
		#print (len(x))
		#print(*result, sep = '\t')
		#from tabulate import tabulate
		#print(tabulate(result))
		#print(x)
	time.sleep(3)

# Menu Item 6
def view_twinned():
	print("View Twinned Cities")
	print ("Twinned Cities")
	print ("--------------")
	connect()
	with driver.session() as session:
		final = session.read_transaction(get_results)
		for x in final:
			print(x)
			#time.sleep(1)
		time.sleep(3)
		#print(final)
def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "rootroot"))
def get_results(tx):
    query = "match(n:City)-[t:TWINNED_WITH]-(n1:City) return n.name, n1.name order by n.name"
    names = []
    names2 = []
    results = tx.run(query)
    for x in results:
        names.append(x['n.name'])
        names2.append(x['n1.name'])
    x=0
    final=[]
    while x < len(names):
        final.append(names[x] + " <-> " + names2[x])
        x=x+1
    return final

# Menu Item 7
def twinned_with_dublin():
	print("Twinning with Dublin")
	city_to_twin = input("Enter ID of City to twin with Dublin : ")
	cursor = db.cursor()
	sql = "select name from city where id = %s"
	values = (city_to_twin,)
	cursor.execute(sql, values)
	result = cursor.fetchall()
	if len(result) == 0:
		print(f"Error: City ID: {city_to_twin} doesn't exist in MySQL Database.")
		time.sleep(3)
	else:
		print("Exists in MySQL, now checking if Dublin still exists in neo4j")
		[new_city]= result
		print("City Name in SQL is: ", new_city[0])
		time.sleep(3)
		connect()
		with driver.session() as session:
			neo4j_exists = session.read_transaction(get_results2)
			#print("Does it exist: ", neo4j_exists)
			new_int=neo4j_exists[0]
			if new_int != [1]:
				print("Error: Dublin does not exist in Neo4j Database")
				time.sleep(3)
			else:
				print("Yes, Dublin still exists - now need to check if the new city exists in neo4j")
				#"match(n:City{name:"Dublin"})-[:TWINNED_WITH]-(n1:City{name:"Cork"}) return count(n)"
				#if not then create it and twin with Dublin
				#"create (:City{cid:999, name:'Cork'})"
				#""
				#if it already exists the just create the relationship
				
				#if it is already twinned then do nothing
				#else
				#create the relationship

			time.sleep(3)

def get_results2(tx):
    query2 = "match(n:City{name:'Dublin'}) return count(n)"
    names3 = []
    results2 = tx.run(query2)
    for x in results2:
        names3.append(x['count(n)'])
    x=0
    final2=[]
    final2.append(names3)
    return final2
	

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
	# https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
	import click
	# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
	from tabulate import tabulate
	from neo4j import GraphDatabase

	driver = None

	db = mysql.connector.connect(
    host=cfg["host"],
    user = cfg["user"],
    password = cfg["password"],
    database = cfg["database"]
)
	# execute only if run as a script 
	main()
