import sys

def getBox(title=None, values=None):
    if title is not None:
        values = [i.strip() for i in values]
        box = f"<td style=\"border: 1px solid black; padding:10px\"> \
        <h4>{title}</h4> \
        <ul> \
        <li>No {values[1]}</li> \
        <li>{values[2]}</li> \
        <li>{values[3]}</li> \
        <li>{values[4]} electron</li> \
        <ul> \
        </td>"
    else:
        box = "<td style=\"border: 1px solid black; padding:10px\"> </td>"

    return box

def readInputFile():
    try:
        with open('./periodic_table.txt', 'r', encoding="utf-8") as file:
            file = file.read().split('\n')
            data = {}
            for line in file:
                if line.strip():
                    elem, attr = line.split("=")
                    attr = [e.strip().split(":")[1] for e in attr.split(",")]
                    data[elem.strip()] = attr
            return data

    except Exception as e:
        print(f"Error Code: {e.__doc__}")
        exit(1)

def periodic_table():
    data = readInputFile()
    brk = [2, 8, 8, 18]
    i = 0
    eighteenPerLine = False
    for e in data:
        if i not in brk :
            print(getBox(e, data[e]))
        else:
            for n in range(18 - i):
                print(getBox())
        i += 1
    return

if __name__ == "__main__":
    periodic_table()