products = [["iphone",6888],["MacPro",14800],["xiaomi6",2499],["Coffee",31],["Book",60],["iphone",5999],["Nike",699]]
Basket = [] 
i = 0

##	Print product list
print("-"*6 + "Product List" + "-"*6)
for record in products:
	record.insert(0,i)
	i += 1
	for info in record:
		print(info,end="\t")
	print()

## Choose operations
while (1):
	print("*"*50)
	opeinput = input("Operations\n1. Add products to your basket \n2. Delete products from your basket \n3. Modify products informations \n4. Search for products\nChose operations to continue: ")

	if opeinput.isdigit() and float(opeinput) >= 1 and float(opeinput) <= 4:
		operation = int(opeinput)
	else:
		print("Please type a integer number between 1 to 4!\n")
		continue

## Add
	if(operation == 1):	
		while (1):
			amount = int(len(Basket)/2)+1
			print("*"*50)
			cosinput = input("Input number 0 to %d to add product to your basket: "%(int(len(products))-1))
			if cosinput.isdigit() and float(cosinput) >= 0 and float(cosinput) <= (int(len(products))-1):
				request = int(cosinput)
			else:
				print("\nPlease type a integer number between 0 to %d!\n"%(len(products)-1))
				continue
			Basket.append(str(amount))
			Basket.append(products[request])

			cont = input("Press q or Q to exit, other keys to continue: ")
			if cont == "q" or cont == "Q":
				break

## Delete
	if(operation == 2 and len(Basket)!= 0):
		amount2 = amount
		while (1):
			print("*"*50)
			delinput = input("Input amount number 1 to %d to delete products from your basket: "%amount2)

			if delinput.isdigit() and float(delinput) >= 1 and float(delinput) <= amount2:
				delete = int(delinput)
				amount2 -= 1
			else:
				print("Please type a integer number between 1 to %d!\n"%amount2)
				continue

			del Basket[(delete-1)*2]
			del Basket[(delete-1)*2]

			if (Basket == []):
				print("There is nothing left in your basket!")
				break
			
			print()
			print("-"*6 + "Your Basket:" + "-"*6)
			amountin = 1
			for i in range(0,len(Basket),2):
				Basket[i] = str(amountin)
				amountin += 1

			for it in Basket:
				if(type(it)==str):
					print(it,end="\t")
				else:
					for a in it:
						print(a,end="\t")
					print()

			print()	
			cont = input("Press q or Q to exit, other keys to continue: ")
			if cont == "q" or cont == "Q":
				break
	elif(operation == 2):
		print("You have nothing in your basket!")

## Modify
	if operation == 3:	
		while(1):
			print("*"*50)
			modinput = input("Input the product number to modify products information: ")

			if modinput.isdigit() and float(modinput) >= 0 and float(modinput) <= len(products):
				modify = int(modinput)
			else:
				print("Please type a integer number between 0 to %d!\n"%(len(products)-1))
				continue

			infomodinput = input("Modify Product Information \n1.Product\n2.Price\n3.Exit\nWhich product information you want to modify: ")
			
			if infomodinput.isdigit() and float(infomodinput) >= 1 and float(infomodinput) <= 3:
				infomodify = int(infomodinput)
			else:
				print("Please type a integer number between 1 to 3!\n")
				continue

			if infomodify == 1:	
				products[modify][infomodify] = input("Changing product name %s to:"%products[modify][infomodify])
			elif infomodify == 2:
				price = input("Changing %s price %s to:"%(products[modify][infomodify-1],products[modify][infomodify]))
				if price.isdigit() and float(price) > 0:
					products[modify][infomodify] = price
				else:
					print("Please type a positive integer number for price!\n")
					continue
			else:
				break

			print("*"*50)
			print("-"*6+"Product List"+"-"*6)
			for record in products:
				for info in record:
					print(info,end="\t")
				print()

			cont = input("Press q or Q to exit, other keys to continue: ")
			if cont == "q" or cont == "Q":
				break

## Search
	if operation == 4:			
		while(1):
			print("*"*50)
			searinput = input("Input the product name to search for product information: \n")

			t = 0
			for item in products:
				if searinput in item:
					t += 1
					for a in item:
						print(a,end="\t")
					print()
			if (t == 0):						
				print("This product in not in market!")

			cont = input("Press q or Q to exit, other keys to continue: ")
			if cont == "q" or cont == "Q":
				break

## Print your basket and total price
	print()
	print("-"*6 + "Your Basket:" + "-"*6)
	summ = 0
	if Basket==[]: 
		print("Your basket is empty, add some products!")
	else:	
		for it in Basket:
			if(type(it)==str):
				print(it,end="\t")
			else:
				for a in it:
					print(a,end="\t")
				print()
				summ += int(a)

		print("-"*30+"\nTotal Money: %d\n"%summ)