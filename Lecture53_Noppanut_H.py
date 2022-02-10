def vatCalculate(totalPrice):
	vat = 7/100
	result = totalPrice+(totalPrice * vat)
	return result


totalPrice = int(input("Enter Price : "))
print("Total Vat Incl. : ", "{:,.2f}".format(vatCalculate(totalPrice)))