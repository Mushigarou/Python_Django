import sys

def findCapital(state):

    capital = "Unknown state"

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
    
    if state in states:
        capital = capital_cities[states[state]]

    print(capital)

if __name__ == "__main__":
    if len(sys.argv[1:]) == 1:
        findCapital(sys.argv[1])