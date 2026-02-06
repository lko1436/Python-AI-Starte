class Stock:
    def __init__(self, name, buy_price):
        self.name = name
        self.buy_price = buy_price
    def calculate_return(self, current_price):
        return ((current_price - self.buy_price) / self.buy_price) * 100
    
my_stock = Stock("006208", 100)
result = my_stock.calculate_return(150)
print(f"{my_stock.name} 的報酬率是: {result}%")