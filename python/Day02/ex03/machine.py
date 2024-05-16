import beverages
import random

class   CoffeeMachine:
    repaired = 1

    class EmptyCup(beverages.HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"

    class   BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")
    
    def repair(self) -> None:
        self.repaired = 1
        pass
    
    def serve(self, cls : beverages) -> None:
        if self.repaired > 10:
            raise CoffeeMachine.BrokenMachineException()
        ret = self.EmptyCup() if random.randint(0, 1) else cls()
        self.repaired += 1
        return ret

def test():
    machine = CoffeeMachine()
    mugs = [beverages.Coffee, beverages.Cappuccino, beverages.Tea, beverages.Chocolate]

    for i in range(10):
        for m in mugs:
            try:
                cof = machine.serve(beverages.Chocolate)
                print(cof)
            except machine.BrokenMachineException as e:
                print(e)
        if i == 5:
            machine.repair()
        

if __name__ == "__main__":
    test()