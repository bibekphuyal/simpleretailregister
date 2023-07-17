#The class name checkoutregister  is declared
class CheckoutRegister:
    #The constructor method init is defiend along with formal parameters
    def __init__(self):
        #Self is an instance of the class CheckoutRegister used to access its attributes
        self.productList = []
        self.shoppingCart = []
        self.total_payment = 0.0
        self.due = 0.0
        self.paymentReceived = 0.0
        self.change = 0.0
        
    #Defining a method to reset the checkout register back to clean slate
    def reset_checkout(self):
        self.productList = []
        self.shoppingCart = []
        self.total_payment = 0.0
        self.due = 0.0
        self.paymentReceived = 0.0
        self.change = 0.0

    #Defining a method to add the products to the productlist
    def add_product(self, prod):
        self.productList.append(prod)

    #Defining a method to display all the products added to the Product List   
    def display_products(self):
        for prod in self.productList:
            print (prod.getpcode() + " - " + prod.getName() + " - $ {:.2f}".format(prod.getPrice()))
            
    #Defining a method to add the product selected by customer to the Shopping List
    def product_scan(self, p_code):
        for prod in self.productList:
            #Checks the product code and if it matches it adds the product to the Shopping List  
            if prod.getpcode()==p_code:
                self.shoppingCart.append(prod)
                return prod.getName() + " has been added to the shopping cart"
        #Error message if the user enters invalid Product code     
        return " Sorry the product is not available"

    #Defining a method to display all the products added to the Shopping List 
    def display_cart(self):
        for prod in self.shoppingCart:
            print (prod.getpcode() + " - " + prod.getName() + " - $ {:.2f}".format(prod.getPrice()))

    #Defining a method to calculate the total price of the products in the Shopping List
    def determine_payment(self):
        value = 0.0
        for prod in self.shoppingCart:
            value = value + float(prod.getPrice()) 
        #Assigning the total price of shopping list to two variables 
        self.total_payment = value
        self.due = value
        #returns the total price when the method is called upon
        return value

    #Defining a method that calculates the change to be given out
    def accept_payment(self, cash):
        self.paymentReceived = self.paymentReceived + cash
        self.change = self.paymentReceived - self.due
        #Returns the amount to be returned to customer when called upon 
        return self.change

    #Defining a method that prints the receipt based on the shopping list
    def print_receipt(self):
        for prod in self.shoppingCart:
            print (prod.getpcode() + " - " + prod.getName() + " - $ {:.2f}".format(prod.getPrice()))
        return self.paymentReceived




    ################ INCORPORATION OF GIVEN CODE ############################


    # preventing user from entering negative cash value
    def get_float(self):
        #Initialize the variable value
        value = float(0.0)
    
        #ask user to insert cash until due amount is cleared
        while True:
            try:
                #gets value from user and assigns it to a variable
                print("")
                value = float (input ("Please Insert Cash: "))

                #If condition is checked for negative value
                if value < 0.0:
                     print("We don't accept negative money!")
                     continue
                #Breaks the while loop
                break 
 
            #Expection handling when user enters value other than float 
            except ValueError:
                print("Please enter a valid floating point value.") 
 
        #Returns the value stored in variable value when called upon
        return value
