import contents
from datetime import date
today = date.today()
file_name = "users_info.txt"

items=[]
def database(user, itemID):
	with open(file_name, "a") as file_object:
		file_object.write("Date of Transaction : "+ str(today) +"\n" +"userID : " + user +"\t"+ "ItemID : "+ itemID + "\n")
	

def load_vm(): 
    global vm1,vm2
    vm1=contents.VendingMachine("A1",10,"Water",2)
    items.append(vm1)  
    vm2=contents.VendingMachine("A2",20,"Chips",4)
    items.append(vm2)

def buy_items(user , userID):
	print("Purchase item")
	print("*"*40)
	purchase_item_id = input("Enter item ID : ")
	
	#Purchase item A1 for employee and student.
	if purchase_item_id == "A1" or purchase_item_id == "a1":
		if vm1.quantity > 0 :
			if user == "Employee":
				try:
					pay = int(input("please pay $10 : "))
					if pay == 10 :
						print("Transcation complete...")
						vm1.quantity -= 1
						database(userID,"A1")
					elif pay <= 10:
						print("Insufficient balance")
					elif pay>= 10:
						print("Transcation complete...")
						vm1.quantity -= 1
						print("Here, is your remaining balance $"+ str(pay-10))
						database(userID, "A1")
				except:
					print("Invalid input")

			elif user == "Student":		
				try:
					pay = int(input("please pay $8 : "))
					if pay == 8 :
						print("Transcation complete...")
						vm1.quantity -= 1
						database(userID,"a1")
					elif pay <= 8:
						print("Insufficient balance")
					elif pay>= 8:
						print("Transcation complete...")
						vm1.quantity -= 1
						print("Here, is your remaining balance $"+ str(pay-8))
						database(userID,"A1")
				except:
					print("Invalid input")

		else:
			print(" Empty Slot for itemID: A1")
	
	#Purchase item A2 for employee and student.
	elif purchase_item_id == "A2" or purchase_item_id == "a2":
		if vm2.quantity > 0 :
			if user == "Employee":
				try:
					pay = int(input("please pay $20 : "))
					if pay == 20 :
						print("Transcation complete...")
						vm2.quantity -= 1
						database(userID,"A2")
					elif pay <= 20:
						print("Insufficient balance")
					elif pay>= 20:
						print("Transcation complete...")
						vm2.quantity -= 1
						print("Here, is your remaining balance $"+ str(pay-20))
						database(userID,"A2")
				except:
					print("Invalid input")

			elif user == "Student":		
				try:
					pay = int(input("please pay $16 : "))
					if pay == 16 :
						print("Transcation complete...")
						vm2.quantity -= 1
						database(userID,"A2")
					elif pay <= 16:
						print("Insufficient balance")
					elif pay>= 16:
						print("Transcation complete...")
						vm2.quantity -= 1
						print("Here, is your remaining balance $"+ str(pay-16))
						database(userID,"A2")
				except:
					print("Invalid input")

		else:
			print(" Empty Slot for itemID: A2")

	else:
		print("invalid item ID")
	
def add_item():
	print("ADD ITEM")
	print("*"*40)
	adding_item = input("Enter item ID: ")
	if adding_item == "A1" or adding_item == "a1":
		print("price : $10 ")
		try:
			number_of_items = int(input("How many items are you adding? :"))
			vm1.quantity += number_of_items
			print("Items added:"+ str(number_of_items))
			print("No of A1 items available now is: "+ str(vm1.quantity))
		except:
			print("Invalid Input")
	elif adding_item == "A2" or adding_item == "a2":
		print("price : $20 ")
		try:
			number_of_items = int(input("How many items are you adding? :"))
			vm2.quantity += number_of_items
			print("Items added:"+ str(number_of_items))
			print("No of A2 items available now is: "+ str(vm1.quantity))
		except:
			print("Invalid Input")
	else:
		print("invalid input")

def display_items():
    count_number_of_items = len(items)
    print("       Contents of VM")
    print("-"*30)
    print("Items in VM (Total: "+str(count_number_of_items)+")")
    print("NO# \t ItemID \tPrice\tItem Name\tQuantity")

    print("\n1.\t"+vm1.itemID+"\t"+"\t"+str(vm1.price)+"\t"+vm1.iname+"\t"+"\t"+str(vm1.quantity))
    print("\n2.\t"+vm2.itemID+"\t"+"\t"+str(vm2.price)+"\t"+vm2.iname+"\t"+"\t"+str(vm2.quantity))
    
def file_reader():
	with open(file_name) as file_object:
		contents = file_object.read()
		print("Details of items sold are : ")
		print("-"*30)
		print(contents)

def file_reset():
	open(file_name, 'w').close()
