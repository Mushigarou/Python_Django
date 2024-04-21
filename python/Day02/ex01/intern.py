class Intern:
    Name = "My name? I’m nobody, an intern, I have no name."
    
    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."
    
    def __init__(self, s=None) -> None:
        if s is not None:
            self.Name = s
    
    def __str__(self) -> str:
        return f"{self.Name}"

    def work(self):
        raise BaseException("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return Intern.Coffee()

def tester():
    obj = Intern()
    obj1 = Intern('Mark')
    print(obj)
    print(obj1)
    try :
        print(obj.work())
    except BaseException as e:
        print(f"{e}")
    print(obj1.make_coffee())

if __name__ == "__main__":
    tester()
