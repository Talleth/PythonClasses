#===================================================================
#    Purpose:   Practice in using simple Python classes
#===================================================================

# Class to define a customer
class Customer:
    def __init__(self):    
        self.name       = None
        self.address    = None
        self.phone      = None
        self.balance    = None

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setPhone(self, phone):
        if len(phone) == 12:
            self.phone = phone
            return True
        else:
            print("Phone number must be 10 digits with dashes")
        return False

    def setBalance(self, balance):
        if int(balance) > 0:
            self.balance = balance
            return True
        else:
            print("No negative balance is allowed.")
            return False

    def printCustomer(self):
        print(self.name,"at",self.address,"and phone number",self.phone,"owes $",self.balance)

# List to hold customers entered by the user
customers = list()

# Collect 5 customers from the user
for i in range(0,5):
    temp = Customer()
    temp.setName(input("Input Name:"))
    temp.setAddress(input("Input Address:"))

    while not temp.setPhone(input("Input Phone:")):
        print("Enter the phone again:")
    while not temp.setBalance(input("Input Balance:")):
        print("Enter the balance again:")

    customers.append(temp)

# Let the user select all or one of the options to display
option = ''

while (option != 'all' and option != 'one'):
    option = str(input("Would you like to see all or one of the customers?  Type 'one' or 'all': "))

if (option == 'all'):
    for customer in customers:
        customer.printCustomer()
else:
    name = str(input("Enter the name to find: "))

    for customer in customers:
        if (customer.name == name):
            customer.printCustomer()
            break