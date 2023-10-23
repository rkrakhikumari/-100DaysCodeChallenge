import csv

class item:
    pay_rate = 0.8 #20% discout
    all =[]
    def __init__(self,name: str, quantity: float ,price:float):

        assert price>=0, f"price {price} should be greater than or eqyal to zero"
        assert quantity>=0, f"quantity {quantity} should be greater than or equal to zero"

        self.name = name
        self.quantity = quantity
        self.price = price

        item.all.append(self)

    def claculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price *self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv' , 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                item(
                    name = item.get('name'),
                    price = float(item.get('price')),
                    quantity = float(item.get('quantity'))
                )


    def __repr__(self):
        return f"item ('{self.name}',{self.price},{self.quantity})"

item.instantiate_from_csv()





        