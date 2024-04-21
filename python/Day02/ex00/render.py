import sys
import os
import re
from settings import Template

def readTemplate(filename: str) -> str:
    try :
        with open(filename, 'r', encoding="utf-8") as file:
            s = file.read()
            file.close()
            return s
    except Exception as e:
        file.close()
        print(f"Code Error: {e}")
        exit(1)

def renderTemplate(cv: str, **kw) -> str:
    for elem in kw:
        cv = cv.replace("{" + elem + "}", kw[elem])
    return cv

def parseFilename() -> str:
    try:
        if len(sys.argv) != 2:
            raise(f"Error: expect 1 argument, {len(sys.argv)-1} were given")
        filename = sys.argv[1]
        if re.search('\.template$', filename) is None:
            raise("Error: expect <.template> extension")
        return filename
    except Exception as e:
        sys.stderr.write(e.__doc__)
        exit(1)

def main():
    filename = parseFilename()
    cv = readTemplate(filename)
    obj = Template()
    render = renderTemplate(cv, **obj.__dict__)
    try:
        s = filename[:filename.find(".template")]
        with open(f"{s}.html", 'w+') as output:
            os.write(output.fileno(), render.encode(encoding="utf-8"))
    except Exception as e:
        print(f"Error Code: {e}")


if __name__ == "__main__":
    main()
