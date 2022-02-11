def showBill():
	nameCafe = "N-Cafe"
	totalPrice = 0
	print(nameCafe.center(15, "*"))
	for i in range(len(listMenu)):
		print(str(i+1) + ".", listMenu[i][0], "Price", listMenu[i][1])
		totalPrice += listMenu[i][1]
	print("Total Price :", totalPrice, "THB")

listMenu = []

while True:
	menuName = input("Please Enter New Menu : ")
	if menuName.capitalize() == "Exit":
		break
	else:
		menuPrice = int(input("Order Price : "))
		listMenu.append([menuName, menuPrice])

showBill()