import sys

def searchByKeyOrValue(input):

    if input.find(",,") != -1:
        return

    # state = "Unknown capital city"
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }    
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    lookfor = list(" ".join(elem.split()) for elem in input.split(',') if elem.strip())
    keys = {e.lower():e for e in list(states.keys())}
    values = [e.lower() for e in list(capital_cities.values())]

    for i in lookfor:
        try: 
            if i.lower() in keys.keys():
                key = states[keys[i.lower()]]
                state = keys[i.lower()]
            else:
                key = list(capital_cities.keys())[values.index(i.lower())]
                state = list(states.keys())[list(states.values()).index(key)]
            print(f"{capital_cities[key]} is the capital of {state}")
        except:
            print(f"{i} is neither a capital city nor a state")

if __name__ == "__main__":
    if len(sys.argv[1:]) == 1:
        searchByKeyOrValue(sys.argv[1])