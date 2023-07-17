#Declaring the class named Product 
class Product:
    #The constructor method init is defiend along with formal parameters 
    def __init__(self, productcode, name, price, weight):
        #Self is an instance of the class Product used to access its attributes
        self.pcode = productcode
        self.name = name
        self.price = price
        self.weight = weight

    #Defining a method named getBar to get the productcode
    def getpcode(self):
        #Returns the value of parameter productcode when called upon 
        return self.pcode

    #Defining a method named getName to get the name of the product
    def getName(self):
        #Returns the value of parameter name when called upon         
        return self.name

    #Defining a method named getPrice to get the price of the product
    def getPrice(self):
        #Returns the value of parameter price when called upon             
        return self.price

    #Defining a method named getWeight to get the weight of the product    
    def getWeight(self):
        #Returns the value of parameter weight when called upon         
        return self.weight
    
