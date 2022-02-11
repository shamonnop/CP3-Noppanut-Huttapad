def showBill():
	nameCafe = "N-Cafe"
	print(nameCafe.center(15, "*"))
	for i in range(len(listMenu)):
		print(str(i + 1) + ". " + listMenu[i] + " Price " + str(listMenuPrice[i]))
	print("Total Price :", sum(listMenuPrice), "THB")

listMenu = []
listMenuPrice = []


while True:
	menuName = input("Please Enter New Menu : ")
	if menuName.lower() == "exit":
		break
	else:
		menuPrice = int(input("Order Price : "))
		listMenu.append(menuName)
		listMenuPrice.append(menuPrice)
print(listMenu)
print(listMenuPrice)
showBill()






