class Customer :
	name = ""
	lName = ""
	#address = ""
	telNo = ""
	#email = ""
	#birthDate = ""
	age = 0
	#gender = ""

	def addCart(self):
		print("Added Product to ", self.name, self.lName, "'s Cart")

customer1 = Customer()
customer1.name = "Noppanut"
customer1.lName = "H"
customer1.addCart()

customer2 = Customer()
customer2.name = "Bee"
customer2.lName = "H"
customer2.addCart()

customer3 = Customer()
customer3.name = "Benz"
customer3.lName = "R"
customer3.addCart()

customer4 = Customer()
customer4.name = "Tan"
customer4.lName = "C"
customer4.addCart()