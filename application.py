import time
import sys
import userFunctions

def loading():

	animation = "|/-\\"

	for i in range(20):
		time.sleep(0.1)
		sys.stdout.write("\r"+"logging in" + animation[i % len(animation)])
		sys.stdout.flush()



def try_user():
	global user
	x = time.sleep(0.5)
	user=input("\n\nPlease enter your \n\t> MIT Employee ID exxx\n\tor \n\t> MIT Student ID sxxx:")
	loading()
	if "e" in user or "E" in user:
		print()
		print("Hello user: "+user)
		print("Welcome to MIT Vending Machine")
	
	elif "s" in user or "S" in user:
		print()
		print("Hello user: "+user)
		print("Welcome to MIT Vending Machine")
	
	else:
		print("Invalid User")

def menuStaff():
    
    print("*"*40)
    print("     Employee Vending Machine    ")
    print("*"*40)
    print("E1. Buy")    
    print("E2. Add")
    print("E3. Display items")
    print("E4. Log out | Quit")
    print("E5. Close the program")
    print("E6. Details of transactions")
    
def menuStudent():
    
    print("*"*40)
    print("     Student Vending Machine    ")
    print("*"*40)
    print("S1. Buy")
    print("S2. Display items") 
    print("S3. Quit")


def main():
	userFunctions.load_vm()
	userFunctions.display_items()
	userFunctions.file_reset()
	try_user()
	while True:
		if "e" in user or "E" in user:
			menuStaff()
			options = input("Your option[E1-E4] : ")
			if options == "E1" or options == "e1":
				userFunctions.buy_items("Employee",user)
				
			elif options =="E2" or options == "e2":
				userFunctions.add_item()
				
			elif options =="E3" or options == "e3":
				userFunctions.display_items()
				
			elif options == "E4" or options == "e4":
				print("Logging out...")
				try_user()

			elif options == "E5" or options =="e5":
				break

			elif options == "E6" or options == "e6":
				userFunctions.file_reader()
				
			else:
				print("Invalid input")

		elif "s" in user or "S" in user:
			menuStudent()
			options = input("Your option[S1-E3] : ")
			if options == "S1" or options == "s1":
				userFunctions.buy_items("Student", user)
				
			elif options =="S2" or options == "s2":
				userFunctions.display_items()
				
			elif options =="S3" or options == "s3":
				print("Logging out...")
				try_user()

			else:
				print("Invalid input")
	
		else:
			try_user()

	



main()