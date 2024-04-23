from account import Account


class Customer(Account):
    def __init__(self, email, password):
        super().__init__(email, password)
        
    def view_product(self, seller):
        for item, quantity in seller.products.items():
            name, price = item
            print(name, price, quantity)
            
    def buy_product(self, seller, pro_name, pro_quantity):
        for item, quantity in seller.products.items():
            name, price = item
            if name == pro_name and pro_quantity <= quantity:
                total_price = price * pro_quantity
                print("===========================")
                print(f"You have purchased {pro_name} || Price: {total_price}")
                print("===========================")
                seller.products[item] -= pro_quantity
                break
        else:
            print("Invalid Input")


class Seller(Account):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = {}
        
    def publish_product(self, name, price, quantity):
        self.products[(name, price)] = quantity


