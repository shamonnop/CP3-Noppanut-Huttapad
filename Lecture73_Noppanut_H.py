dictDrinkMenu = {"Americano": 55, "Latte": 65, "Cappuccino": 70, "Mocha": 85, "Chocolate": 65, "Tea": 55, "Lemonade": 50}
listDrinkMenu = list(dictDrinkMenu.keys())
listMenu = []
nameCafe = "N-Cafe"

def showBill():
	totalPrice = 0
	print(nameCafe.center(23, "*"))
	for i in range(len(listMenu)):
		print(str(i+1) + ".", listMenu[i][0], "/ Price :", listMenu[i][1])
		totalPrice += listMenu[i][1]
	print("Total Price :", totalPrice, "THB")
	print("***Thank you and Have a nice day***")

def showMenu():
	print(nameCafe.center(23, "*"))
	for i in range(len(listDrinkMenu)):
		print(str(i+1) + ".", listDrinkMenu[i], "/ Price :", dictDrinkMenu[listDrinkMenu[i]])
	print("*********************")

showMenu()
while True:
	menuSelect = int(input("Please Enter The Number of Menu (or 0) : "))
	if menuSelect == 0:
		break
	elif menuSelect >= len(listDrinkMenu)+1:
		print("Please Enter Menu Again")
	else:
		indexlistDrinkMenu = listDrinkMenu[menuSelect-1]
		print(indexlistDrinkMenu, "/ Price :", dictDrinkMenu[indexlistDrinkMenu])
		listMenu.append([indexlistDrinkMenu, dictDrinkMenu[indexlistDrinkMenu]])

showBill()