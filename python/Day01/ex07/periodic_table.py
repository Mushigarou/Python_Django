import sys

def getBox(title=None, values=None) -> str:
    if title is not None:
        values = [i.strip() for i in values]
        box = f"<td style=\"border: 1px solid black; padding:10px\"><h4>{title}</h4><ul><li>No {values[1]}</li><li>{values[2]}</li><li>{values[3]}</li><li>{values[4]} electron</li></ul></td>"
    else:
        box = "<td style=\"padding:10px\"> </td>"

    return box

def readInputFile() -> dict:
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

def printRow(data: dict, brkpoint: int, startIndex: int, file) -> None:

    keys = []
    i = 0
    emptyBoxes = ["".join(getBox()) for n in range(18 - brkpoint)]
    file.write("<tr>")
    for e in data:
        if (i == brkpoint):
            break
        if (i == startIndex) and len(emptyBoxes) > 0:
            [file.write(box) for box in emptyBoxes]
        file.write(getBox(e, data[e]))
        keys.append(e)
        i += 1
    [data.pop(k) for k in keys]
    file.write("</tr>")

    return

def periodic_table() -> None:
    try :
        with open("periodic_table.html", "x") as file:
            data = readInputFile()
            brk = [8, 8, 18, 18, 18, 18]
            startSpaceIndex = 2

            file.write("<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Periodic Table</title></head><body><table>")
            printRow(data, 2, 1, file) # prints first row
            for i in brk:
                printRow(data, i, startSpaceIndex, file)
            file.write("</table></body></html>")
    except Exception as e:
        print(f"Error Code: {e.__doc__}")

if __name__ == "__main__":
    periodic_table()
