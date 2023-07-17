#Imports class Prodcut and Checkout to this file 
from product import Product
from checkoutregister import CheckoutRegister

#Defines the method main 
def main():
    

    
    
    # calls the init method of Product class
    item_a = Product("111", " juice", 3.0, 4.0)
    item_b = Product("222", " chicken", 7.5, 8.0) 
    
    #calls the init method of Checkout class
    checkout = CheckoutRegister()
   
    #Adding products to the product list 
    checkout.add_product(item_a)
    checkout.add_product(item_b)
    
    #Calls the method to display products from the Checkout class
    print ("Product Code  Product Name   Price ")
    checkout.display_products()
   
    

    #While loop begins
    while True:
        
       #prompt user to enter the product code
       print("")
       pcode = input ("Enter the product code of the Product: ")

       #product is added to the cart and displayed to user 
       message = checkout.product_scan(pcode)      
       print(message)
       print("")
       
       #prompt user to scan more products or move to checkout
       more = input ("Enter any key to add product or enter N to quit: ")
       if(more == "N" or more == "n"):
           break # break out of the loop



    


    #Calls the method to display the list of products in the shopping cart 
    checkout.display_cart()

    #Calls the method to get the total amount from checkout class
    due = checkout.determine_payment()
    print("")
    print("")
    print("Due Amount     : ${0}".format(due))
    print("")
    print("")

   
    #prompt user to enter cash until due amount is cleared 
    while True:
       cash = checkout.get_float()
       #Passes the value of cash to the function and assigns the return value to change
       change  = float (checkout.accept_payment(cash))
       #if command that controls the while loop 
       if (change >= 0):
           #breaks the while loop
           break
  

    #Calls the method to print the receipt 
    amount = checkout.print_receipt()
    print("")
    print("")
    print("Due Amount     : ${0}".format(due))
    print("")
    print("Cash           : ${0}".format(amount))
    print("")
    print("Cash Change    : ${0}".format(change))
    print("")
    print("")
    print("Thank you for shopping with us. ")
    print("")
    print("")
           


    #prompt user whether to scan more products or move to checkout
    more = input ("Enter any key or enter Q to quit: ")
    if(more == "Q" or more == "q"):
        exit
    else:
        #Calls the method to reset the Checkout register to be used by next customer
        checkout.reset_checkout()

       
        #Calls the main method
        main()
    
#Calls the method main that starts the whole program
main()    
