def getDataFromFile():
    try:
        with open("./numbers.txt", "r", encoding="utf-8") as file:
            bytes = file.read()
            file.close()
            return bytes
    except Exception as e:
        print(f"Error Code: {e.__doc__}")

def printNumbers():
    return [print(i) for i in getDataFromFile().split(",") if i != "\n"]

if __name__ == "__main__":
    printNumbers()