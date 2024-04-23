from users import *


customer_list = []
seller_list = []

while True:
    print("""1. Sign up as a Customer
2. Sign up as a Seller
3. Login
4. Exit
    """)
    n = int(input("Enter Option: "))
    
    if n == 1:
        mail = input("Enter your mail: ")
        password = input("Enter your password: ")
        email_registered = any(customer.email == mail for customer in customer_list)
        if not email_registered:
            temp = Customer(mail, password)
            customer_list.append(temp)
            print("=====================================")
            print("Sign up successful!")
            print("=====================================")
        else:
            print("=====================================")
            print("You have already created your account")
            print("=====================================")
            
    elif n == 2:
        mail = input("Enter your mail: ")
        password = input("Enter your password: ")
        email_registered = any(seller.email == mail for seller in seller_list)
        if not email_registered:
            temp = Seller(mail, password)
            seller_list.append(temp)
            print("=====================================")
            print("Sign up successful!")
            print("=====================================")
        else:
            print("=====================================")
            print("You have already created your account")
            print("=====================================")
        
    elif n == 3:
        print("1. Customer")
        print("2. Seller")
        k = int(input("Enter your option: "))
        
        if k == 1:
            mail = input("Enter your mail: ")
            password = input("Enter your password: ")
            
            for temp in customer_list:
                if temp.email == mail and temp.password == password:
                    print("*************************************")
                    print("""1. View product
                2. Place order
                3. Exit
                      """)
                
                    m = int(input("Enter Option: "))
                    if m == 1:
                        # Assuming there's a seller object selected by the customer
                        seller_index = int(input("Enter seller index: ")) - 1
                        if 0 <= seller_index < len(seller_list):
                            temp.view_product(seller_list[seller_index])
                        else:
                            print("Invalid seller index")
                    elif m == 2:
                        pro_name = input("Enter product name: ")
                        pro_quantity = int(input("Enter product quantity: "))
                        # Assuming the customer selects a seller from the list
                        seller_index = int(input("Enter seller index: ")) - 1
                        if 0 <= seller_index < len(seller_list):
                            temp.buy_product(seller_list[seller_index], pro_name, pro_quantity)
                        else:
                            print("Invalid seller index")
                    elif m == 3:
                        break
                    else:
                        print("Invalid Option")
                    break
            else:
                print("Invalid Credentials")
        
        elif k == 2:
            mail = input("Enter your mail: ")
            password = input("Enter your password: ")
            
            for temp in seller_list:
                if temp.email == mail and temp.password == password:
                    print("Publish your product--->")
                    
                    product_name = input("Product name: ")
                    product_price = float(input("Product price: "))
                    product_quantity = int(input("Product quantity: "))
                    
                    temp.publish_product(product_name, product_price, product_quantity)
                    print("Product has been added")
                    break
            else:
                print("Invalid Credentials")
            
    elif n == 4:
        break
