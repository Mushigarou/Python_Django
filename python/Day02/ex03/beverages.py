class   HotBeverage:
    price = 0.30
    name = "hot beverage"
        
    def description(self) -> str:
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        x = "{:.2f}".format(self.price)
        return f"name : {self.name}\nprice : {x}\ndescription : {self.description()}"

class   Coffee(HotBeverage):
    name = "coffee"
    price = 0.40
    
    def description(self) -> str:
        return "A coffee, to stay awake."

class   Tea(HotBeverage):
    name = "tea"
    price = 0.30

class   Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50

    def description(self) -> str:
        return "Chocolate, sweet chocolate..."

class   Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45

    def description(self) -> str:
        return "Un po' di Italia nella sua tazza!"

def test():
    objs = [HotBeverage, Coffee, Tea, Chocolate, Cappuccino]
    for obj in objs:
        ins = obj()
        print(ins, "\n")

if __name__ == "__main__":
    test()