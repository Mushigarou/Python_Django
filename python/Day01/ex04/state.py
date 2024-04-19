import sys

def findCapital(cap):

    state = "Unknown capital city"

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

    try:
        city = list(capital_cities.keys())[list(capital_cities.values()).index(cap)]
        state = list(states.keys())[list(states.values()).index(city)]
    except:
        print(state)
        return

    print(state)

if __name__ == "__main__":
    if len(sys.argv[1:]) == 1:
        findCapital(sys.argv[1])